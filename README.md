# Big Data MapReduce, Mahout Clustering, and Ticket Similarity

This project is a cleaned portfolio version of a Big Data analytics pipeline. It combines Hadoop Streaming, Apache Mahout, and transformer-based NLP across three different tasks: weather data analysis, document clustering, and IT ticket similarity detection.

The goal was not just to run tools, but to build end-to-end data workflows: clean the input, process it at scale, generate outputs, compare results, and explain the decisions behind each approach.

## What this project covers

### 1. Weather Data Analysis with Hadoop Streaming

The first part uses Python mappers and reducers with Hadoop Streaming to analyse hourly weather data.

It calculates:

- daily Dry Bulb Temperature statistics
- daily Wind Speed statistics
- station-level mean, variance, standard deviation, minimum, and maximum
- covariance and correlation between weather variables
- simple linear regression
- two-variable regression
- MSE and RMSE model comparison

This section shows how basic statistical analysis can be built using MapReduce without relying on ready-made statistical libraries.

### 2. Document Clustering with Apache Mahout

The second part clusters a collection of literary text documents using Apache Mahout K-Means.

The workflow includes:

- cleaning and preparing the text documents
- removing common English and French stopwords
- converting text files into Hadoop sequence files
- generating TF-IDF sparse vectors
- running K-Means with different values of K
- comparing Euclidean and Manhattan distance measures
- interpreting clusters using top TF-IDF terms

The final selected setup was Manhattan Distance with K = 5 because it gave the clearest cluster terms and the most interpretable document themes.

### 3. IT Ticket Similarity with Sentence Transformers

The third part compares pairs of IT support tickets using transformer embeddings.

The mapper reads ticket pairs and the reducer:

- loads a locally packaged Sentence Transformer model
- creates embeddings for both ticket descriptions
- calculates cosine similarity
- applies a threshold-based similarity rule
- outputs a True/False similarity label

The model used was `all-MiniLM-L6-v2`. It was packaged locally for Hadoop execution because the worker nodes did not have internet access.

## Tech stack

- Python 3
- Hadoop Streaming
- Apache Mahout
- TF-IDF vectorization
- K-Means clustering
- Sentence Transformers
- Cosine similarity
- Shell scripting

## Repository structure

```text
q1_weather_mapreduce/
    Python mapper and reducer scripts for weather analysis

q2_document_clustering_mahout/
    Mahout command script, stopwords, experiment summaries, and cluster extracts

q3_ticket_similarity_transformers/
    Mapper/reducer scripts for ticket similarity using transformer embeddings

docs/
    Screenshots, report material, and selected evidence

assets/
    Optional diagrams or supporting images
