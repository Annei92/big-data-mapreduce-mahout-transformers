#!/usr/bin/env python3
import sys
import csv
import hashlib

reader = csv.reader(sys.stdin)

for row_index, row in enumerate(reader):
    if len(row) < 2:
        continue

    ticket1 = row[0].strip()
    ticket2 = row[1].strip()

    if not ticket1 or not ticket2:
        continue

    # Skip header row exactly.
    if ticket1.lower().strip() == "ticket 1" and ticket2.lower().strip() == "ticket 2":
        continue

    # Stable row ID based on both ticket texts.
    row_id = hashlib.md5((ticket1 + ticket2).encode("utf-8")).hexdigest()[:10]

    ticket1 = ticket1.replace("\t", " ").replace("\n", " ")
    ticket2 = ticket2.replace("\t", " ").replace("\n", " ")

    print(f"{row_id}\t{ticket1}\t{ticket2}")
