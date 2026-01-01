diff --git a/src/build_graph.py b/src/build_graph.py
new file mode 100644
index 0000000000000000000000000000000000000000..b992a8cf334e688ab4910e42b7808ac9e0b79d7a
--- /dev/null
+++ b/src/build_graph.py
@@ -0,0 +1,109 @@
+import argparse
+import csv
+from collections import Counter
+from pathlib import Path
+
+import networkx as nx
+
+
+def parse_list(value):
+    if not value:
+        return []
+    return [item.strip() for item in value.split(",") if item.strip()]
+
+
+def load_posts(path):
+    posts = []
+    with path.open(newline="", encoding="utf-8") as handle:
+        reader = csv.DictReader(handle)
+        for row in reader:
+            row["mentions"] = parse_list(row.get("mentions", ""))
+            row["hashtags"] = parse_list(row.get("hashtags", ""))
+            posts.append(row)
+    return posts
+
+
+def build_graph(posts):
+    graph = nx.DiGraph()
+    interaction_counts = Counter()
+
+    for post in posts:
+        author = post["user"].strip()
+        graph.add_node(author, node_type="account")
+
+        for mention in post["mentions"]:
+            graph.add_node(mention, node_type="account")
+            graph.add_edge(author, mention, edge_type="mention")
+            interaction_counts[(author, mention, "mention")] += 1
+
+        reply_to = post.get("reply_to", "").strip()
+        if reply_to:
+            graph.add_node(reply_to, node_type="account")
+            graph.add_edge(author, reply_to, edge_type="reply")
+            interaction_counts[(author, reply_to, "reply")] += 1
+
+        reshared_from = post.get("reshared_from", "").strip()
+        if reshared_from:
+            graph.add_node(reshared_from, node_type="account")
+            graph.add_edge(author, reshared_from, edge_type="reshare")
+            interaction_counts[(author, reshared_from, "reshare")] += 1
+
+        for hashtag in post["hashtags"]:
+            tag_node = f"#{hashtag.lstrip('#')}"
+            graph.add_node(tag_node, node_type="hashtag")
+            graph.add_edge(author, tag_node, edge_type="uses")
+            interaction_counts[(author, tag_node, "uses")] += 1
+
+    for (source, target, edge_type), count in interaction_counts.items():
+        graph[source][target]["weight"] = count
+        graph[source][target]["edge_type"] = edge_type
+
+    return graph
+
+
+def summarize_graph(graph, top_n):
+    degree_centrality = nx.degree_centrality(graph)
+    betweenness = nx.betweenness_centrality(graph)
+
+    top_degree = sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n]
+    top_betweenness = sorted(betweenness.items(), key=lambda item: item[1], reverse=True)[:top_n]
+
+    return top_degree, top_betweenness
+
+
+def render_summary(top_degree, top_betweenness):
+    print("Top degree centrality:")
+    for node, score in top_degree:
+        print(f"  {node}: {score:.3f}")
+
+    print("\nTop betweenness centrality:")
+    for node, score in top_betweenness:
+        print(f"  {node}: {score:.3f}")
+
+
+def main():
+    parser = argparse.ArgumentParser(description="Build an influence graph from post data.")
+    parser.add_argument("input", type=Path, help="Path to the CSV dataset.")
+    parser.add_argument(
+        "--output",
+        type=Path,
+        default=Path("influence_graph.graphml"),
+        help="Where to write the graph output.",
+    )
+    parser.add_argument("--top", type=int, default=5, help="Number of top nodes to show.")
+    args = parser.parse_args()
+
+    posts = load_posts(args.input)
+    if not posts:
+        raise SystemExit("No posts found in the input dataset.")
+
+    graph = build_graph(posts)
+    top_degree, top_betweenness = summarize_graph(graph, args.top)
+    render_summary(top_degree, top_betweenness)
+
+    nx.write_graphml(graph, args.output)
+    print(f"\nGraph written to {args.output}")
+
+
+if __name__ == "__main__":
+    main()
