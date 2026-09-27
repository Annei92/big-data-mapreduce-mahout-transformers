# Q2 Document Clustering with Apache Mahout

This folder contains the Apache Mahout K-Means document clustering workflow.

The task uses a cleaned text corpus, converts it into sequence files and TF-IDF sparse vectors, then runs K-Means clustering with different K values and distance measures.

## Included Files

- `run_q2_commands.sh` — Mahout command script for sequence file creation, TF-IDF vectorization, K-Means runs, and clusterdump.
- `q2_stopwords.txt` — English and French stopword list used during preprocessing.
- `q2_dataset_counts.txt` — final cleaned document counts.
- `q2_experiment_summary.csv` — summary of K-Means runs for K=3, K=4, and K=5 with Euclidean and Manhattan distance.
- `q2_cluster_terms_summary.csv` — top-term summaries used to interpret clusters.
- `extracts/` — selected clean top-term extracts from cluster dump outputs.

## Selected Model

The selected clustering setup was:

- Distance measure: Manhattan Distance
- K: 5
- Input: stopword-cleaned TF-IDF vectors

This model was selected because it produced the clearest top-term separation across English prose, French theatre, French tragedy, and courtly drama themes.
