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

    # Skip header row wherever it appears.
    if row[0].strip() == "Wban Number":
        continue

    date = row[1].strip()
    dry_temp = clean_number(row[8])
    wind_speed = clean_number(row[12])

    if not date:
        continue

    if len(date) == 8 and date.isdigit():
        date = f"{date[0:4]}-{date[4:6]}-{date[6:8]}"

    if dry_temp is None and wind_speed is None:
        continue

    dry_out = "" if dry_temp is None else str(dry_temp)
    wind_out = "" if wind_speed is None else str(wind_speed)

    print(f"{date}\t{dry_out},{wind_out}")
