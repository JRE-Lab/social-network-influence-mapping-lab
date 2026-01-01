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

+
+---
+
+## Contents
+
+- [Overview](#overview)
+- [Workflow](#workflow)
+- [Repository structure](#repository-structure)
+- [Quick start](#quick-start)
+- [Data schema](#data-schema)
+- [Next steps](#next-steps)
+
+---
 

+## Workflow
+
+1. **Collect**: Export public posts into a CSV.
+2. **Normalize**: Ensure each row contains an author and interactions.
+3. **Build the graph**: Use the provided script to generate GraphML.
+4. **Assess influence**: Review rankings or visualize in Gephi.
+5. **Brief**: Summarize key accounts, clusters, and alternatives.
+
+---
+
+## Repository structure
+
+```
+.
+├── data/
+│   └── sample_posts.csv
+├── src/
+│   └── build_graph.py
+└── requirements.txt
+```
+
+---
+
+## Quick start
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
+python src/build_graph.py data/sample_posts.csv \
+  --output influence_graph.graphml \
+  --top 5
+```
+
+The script prints the top accounts/hashtags by **degree** and **betweenness**
+centrality, then writes `influence_graph.graphml` for tools like **Gephi**.
+
+---
+
+## Data schema
+
+Use a CSV with these headers:
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
+**Example row:**
+
+```csv
+post_id,user,text,mentions,reply_to,reshared_from,hashtags
+42,atlaswatch,"Shipping delays reported.",harborintel,,,#logistics,trade
+```
+
+---
 
-- **Define the scope**: Choose a topic or region and specify the time period and platforms to examine.
-- **Collect OSINT**: Use tools like `snscrape`, platform APIs or search to gather public posts, comments or hashtags related to your topic.
-- **Ingest and normalise**: Parse posts into a structured dataset with entities (users, hashtags) and interactions (mentions, replies, retweets).
-- **Build a graph**: Use Python and NetworkX to create a graph where nodes represent entities and edges represent interactions. Calculate centrality metrics to identify influential accounts.
-- **Analyse and brief**: Interpret the network structure to highlight clusters, key influencers and propagation pathways. Apply abductive reasoning to consider alternative explanations and record confidence levels.
+## Next steps
 
-All data in this lab is gathered from public sources. No private or sensitive data is required.
+- Replace `data/sample_posts.csv` with your collected dataset.
+- Add node attributes (language, location, timestamp) for deeper analysis.
+- Run clustering (e.g., Louvain) to identify communities.
+- Export findings into your briefing template.
