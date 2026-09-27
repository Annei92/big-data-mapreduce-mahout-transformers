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
    if len(row) < 10:
        continue

    if row[0].strip() == "Wban Number":
        continue

    # x = Dew Point Temp
    # y = Dry Bulb Temp
    y = clean_number(row[8])
    x = clean_number(row[9])

    if x is None or y is None:
        continue

    print(f"simple_regression\t{x},{y}")
