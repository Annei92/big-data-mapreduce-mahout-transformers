#!/bin/bash

# Q2 Mahout K-Means document clustering commands
# Dataset: UoL western_classics text dataset
# Final cleaned local folder: q2_docs_sw
# Final cleaned HDFS folder: /user/ainti001/input_q2/q2_docs_sw
# Final results folder: q2_results_sw

mkdir -p q2_results_sw

# 1. Convert cleaned text documents to sequence files
hadoop fs -rm -r -f /user/ainti001/output_q2/seqfiles_sw

mahout seqdirectory \
  -i /user/ainti001/input_q2/q2_docs_sw \
  -o /user/ainti001/output_q2/seqfiles_sw \
  -ow

# 2. Convert sequence files to TF-IDF sparse vectors
hadoop fs -rm -r -f /user/ainti001/output_q2/vectors_sw

mahout seq2sparse \
  -i /user/ainti001/output_q2/seqfiles_sw \
  -o /user/ainti001/output_q2/vectors_sw \
  -wt tfidf \
  -lnorm \
  -nv \
  -ow

# 3. Run K-Means using three K values and two distance measures
for DIST_NAME in euclidean manhattan
do
  if [ "$DIST_NAME" = "euclidean" ]; then
    DIST_CLASS="org.apache.mahout.common.distance.EuclideanDistanceMeasure"
  else
    DIST_CLASS="org.apache.mahout.common.distance.ManhattanDistanceMeasure"
  fi

  for K in 3 4 5
  do
    OUT="/user/ainti001/output_q2/kmeans_${DIST_NAME}_k${K}_sw_seq"
    LOCAL_OUT="q2_results_sw/${DIST_NAME}_k${K}_sw_seq_clusters.txt"
    LOG_OUT="q2_results_sw/kmeans_${DIST_NAME}_k${K}_sw_seq.log"

    echo "Running ${DIST_NAME} K=${K}"

    hadoop fs -rm -r -f "$OUT"

    mahout kmeans \
      -i /user/ainti001/output_q2/vectors_sw/tfidf-vectors \
      -c "$OUT/clusters" \
      -o "$OUT/output" \
      -k "$K" \
      -dm "$DIST_CLASS" \
      -x 20 \
      -cd 0.01 \
      -ow \
      -cl \
      -xm sequential 2>&1 | tee "$LOG_OUT"

    FINAL_CLUSTER_PATH=$(hadoop fs -ls "$OUT/output" | awk '{print $8}' | grep 'clusters-.*-final' | tail -1)

    echo "Final cluster path: $FINAL_CLUSTER_PATH"

    mahout clusterdump \
      -i "$FINAL_CLUSTER_PATH" \
      -p "$OUT/output/clusteredPoints" \
      -o "$LOCAL_OUT" \
      -d /user/ainti001/output_q2/vectors_sw/dictionary.file-0 \
      -dt sequencefile \
      -b 20 \
      -n 20

    echo "Done ${DIST_NAME} K=${K}"
    echo "--------------------------------"
  done
done
