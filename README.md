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
