#!/usr/bin/env python3
import sys
import csv
import re

SLOPE_M = 0.7692548521256619
INTERCEPT_B = 23.330856133079426

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
    # y = actual Dry Bulb Temp
    y = clean_number(row[8])
    x = clean_number(row[9])

    if x is None or y is None:
        continue

    y_pred = (SLOPE_M * x) + INTERCEPT_B
    error = y - y_pred
    squared_error = error * error

    print(f"simple_mse\t{squared_error}")
