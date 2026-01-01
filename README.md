# Social Network Influence Mapping Lab

This lab guides analysts through building a social network influence map using publicly available data. It shows how to collect social media posts, build a graph of interactions and identify key influencers.

## Overview

You will:

- **Define the scope**: Choose a topic or region and specify the time period and platforms to examine.
- **Collect OSINT**: Use tools like `snscrape`, platform APIs or search to gather public posts, comments or hashtags related to your topic.
- **Ingest and normalise**: Parse posts into a structured dataset with entities (users, hashtags) and interactions (mentions, replies, retweets).
- **Build a graph**: Use Python and NetworkX to create a graph where nodes represent entities and edges represent interactions. Calculate centrality metrics to identify influential accounts.
- **Analyse and brief**: Interpret the network structure to highlight clusters, key influencers and propagation pathways. Apply abductive reasoning to consider alternative explanations and record confidence levels.

All data in this lab is gathered from public sources. No private or sensitive data is required.


+## Lab workflow
+
+1. **Collect**: Export public posts into a CSV.
+2. **Normalize**: Ensure each row contains an author, interactions, and metadata.
+3. **Build the graph**: Use the provided script to generate a GraphML network.
+4. **Assess influence**: Review the centrality rankings and visualize the graph in a tool like Gephi.
+5. **Brief**: Summarize the top influencers, clusters, and alternative explanations.
+
+## Repository structure
+
+- `data/sample_posts.csv`: Sample dataset with posts, mentions, replies, reshares, and hashtags.
+- `src/build_graph.py`: Script that constructs the influence graph and prints top influencers.
+- `requirements.txt`: Python dependencies.
+
+## Getting started
+
+### 1) Create a virtual environment (optional)
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+```
+
+### 2) Install dependencies
+
+```bash
+pip install -r requirements.txt
+```
+
+### 3) Run the lab script
+
+```bash
+python src/build_graph.py data/sample_posts.csv --output influence_graph.graphml --top 5
+```
+
+The script prints the top accounts/hashtags by degree and betweenness centrality, then writes a GraphML file you can load into Gephi.
+
+## Data format
+
+Use a CSV with the following headers:
+
+| Column | Description |
+| --- | --- |
+| `post_id` | Unique identifier for the post |
+| `user` | Account that authored the post |
+| `text` | Post text (optional for analysis) |
+| `mentions` | Comma-separated list of mentioned accounts |
+| `reply_to` | Account the post replies to |
+| `reshared_from` | Account the post reshared/retweeted |
+| `hashtags` | Comma-separated list of hashtags |
+
+## Next steps
+
+- Replace `data/sample_posts.csv` with your collected dataset.
+- Add additional node attributes (language, location, timestamp) for deeper analysis.
+- Use graph clustering (e.g., Louvain) to identify communities.
+- Export summary findings into a briefing template.
