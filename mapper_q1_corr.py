#!/usr/bin/env python3
import sys
import csv
import re

def clean_number(value):
    if value is None:
        return None

    value = value.strip()

    if value == "" or value == "-" or value.upper() in {"M", "NA", "N/A", "NULL"}:
        return None

    match = re.search(r"-?\d+(\.\d+)?", value)
    if not match:
        return None

    try:
        return float(match.group(0))
    except ValueError:
        return None

reader = csv.reader(sys.stdin, skipinitialspace=True)

for row in reader:
    if len(row) < 13:
        continue

    # Skip header row.
    if row[0].strip() == "Wban Number":
        continue

    dry = clean_number(row[8])        # Dry Bulb Temp
    dew = clean_number(row[9])        # Dew Point Temp
    humidity = clean_number(row[11])  # % Relative Humidity

    if dry is None:
        continue

    if dew is not None:
        print(f"dry_vs_dewpoint\t{dry},{dew}")

    if humidity is not None:
        print(f"dry_vs_humidity\t{dry},{humidity}")
