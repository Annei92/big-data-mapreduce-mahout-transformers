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

    if row[0].strip() == "Wban Number":
        continue

    # y  = Dry Bulb Temp
    # x1 = Dew Point Temp
    # x2 = Relative Humidity
    y = clean_number(row[8])
    x1 = clean_number(row[9])
    x2 = clean_number(row[11])

    if y is None or x1 is None or x2 is None:
        continue

    print(f"multi_regression\t{x1},{x2},{y}")
