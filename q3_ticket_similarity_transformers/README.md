# Q3 IT Ticket Similarity with Sentence Transformers

This folder contains a Hadoop Streaming workflow for comparing pairs of IT support tickets using transformer embeddings.

The mapper reads ticket pairs from a CSV file and emits a row ID with both ticket descriptions. The reducer loads a locally packaged Sentence Transformer model, creates embeddings for both tickets, calculates cosine similarity, and applies a threshold-based similarity rule.

## Included Files

- `mapper_q3.py` — reads ticket pairs, skips invalid rows, creates row IDs, and emits cleaned ticket text.
- `reducer_q3.py` — loads the Sentence Transformer model, calculates cosine similarity, and outputs similarity labels.
- `q3_threshold_notes.txt` — explains the selected similarity threshold.
- `outputs/` — contains a small sample of the final similarity output.

## Model

The reducer used the `all-MiniLM-L6-v2` Sentence Transformer model.

The model was packaged locally during Hadoop execution because the worker nodes did not have internet access.

## Output Format

```text
row_id    ticket_1    ticket_2    similarity_score    is_similar
