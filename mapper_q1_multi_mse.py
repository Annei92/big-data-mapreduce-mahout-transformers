#!/usr/bin/env python3
import sys
import csv
import re

B0 = 46.07924335451256
B1 = 1.0344088450230822
B2 = -0.5224847933246652

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

    y = clean_number(row[8])    # Dry Bulb Temp
    x1 = clean_number(row[9])   # Dew Point Temp
    x2 = clean_number(row[11])  # Relative Humidity

    if y is None or x1 is None or x2 is None:
        continue

    y_pred = B0 + (B1 * x1) + (B2 * x2)
    error = y - y_pred
    squared_error = error * error

    print(f"multi_mse\t{squared_error}")
	
