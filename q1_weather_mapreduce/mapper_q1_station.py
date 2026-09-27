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

    station = row[0].strip()
    dry_temp = clean_number(row[8])
    wind_speed = clean_number(row[12])

    if not station:
        continue

    if dry_temp is None and wind_speed is None:
        continue

    dry_out = "" if dry_temp is None else str(dry_temp)
    wind_out = "" if wind_speed is None else str(wind_speed)

    print(f"{station}\t{dry_out},{wind_out}")

