# Big Data MapReduce, Mahout Clustering, and Ticket Similarity Pipeline

This repository contains a cleaned portfolio version of a Big Data analytics project built with Hadoop Streaming, Apache Mahout, and transformer-based NLP.

The project demonstrates three workflows:

1. **Weather Data Analysis with MapReduce**  
   Python mapper and reducer scripts calculate daily and station-level weather statistics, covariance/correlation, simple regression, multiple regression, and MSE/RMSE model evaluation.

2. **Document Clustering with Apache Mahout**  
   A text corpus is pre-processed, converted into sequence files and TF-IDF sparse vectors, then clustered using Mahout K-Means with multiple K values and distance measures.

3. **IT Ticket Similarity with Sentence Transformers**  
   Pairs of support tickets are embedded using a Sentence Transformer model, compared using cosine similarity, and classified with a threshold-based similarity rule.

The repository includes source code, command scripts, selected output samples, cluster summaries, screenshots, and documentation. Large raw datasets, full Hadoop output folders, and model binaries are excluded.
