#!/usr/bin/env python3
import os

# Force offline execution in Hadoop worker containers.
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HOME"] = "/tmp/hf_cache_ainti001"
os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache_ainti001"
os.environ["SENTENCE_TRANSFORMERS_HOME"] = "/tmp/hf_cache_ainti001"

import sys
import math
from sentence_transformers import SentenceTransformer

THRESHOLD = 0.65

MODEL_PATH = "model"
model = SentenceTransformer(MODEL_PATH, cache_folder=".")

def cosine_similarity(vec1, vec2):
    dot = 0.0
    norm1 = 0.0
    norm2 = 0.0

    for a, b in zip(vec1, vec2):
        a = float(a)
        b = float(b)
        dot += a * b
        norm1 += a * a
        norm2 += b * b

    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0

    return dot / (math.sqrt(norm1) * math.sqrt(norm2))

print("row_id\tticket_1\tticket_2\tsimilarity_score\tis_similar")

for line in sys.stdin:
    line = line.rstrip("\n")

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) < 3:
        continue

    row_id = parts[0]
    ticket1 = parts[1]
    ticket2 = parts[2]

    embeddings = model.encode([ticket1, ticket2])
    score = cosine_similarity(embeddings[0], embeddings[1])
    is_similar = score >= THRESHOLD

    print(
        f"{row_id}\t"
        f"{ticket1}\t"
        f"{ticket2}\t"
        f"{score:.4f}\t"
        f"{is_similar}"
    )
