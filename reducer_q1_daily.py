#!/usr/bin/env python3
import sys
import math

current_date = None

dry_count = 0
dry_sum = 0.0
dry_sumsq = 0.0
dry_min = None
dry_max = None

wind_count = 0
wind_sum = 0.0
wind_max = None

def reset():
    global dry_count, dry_sum, dry_sumsq, dry_min, dry_max
    global wind_count, wind_sum, wind_max

    dry_count = 0
    dry_sum = 0.0
    dry_sumsq = 0.0
    dry_min = None
    dry_max = None

    wind_count = 0
    wind_sum = 0.0
    wind_max = None

def emit(date):
    if date is None:
        return

    if dry_count > 0:
        dry_mean = dry_sum / dry_count
        dry_variance = (dry_sumsq / dry_count) - (dry_mean * dry_mean)

        # Avoid tiny negative values caused by floating-point precision.
        if dry_variance < 0 and dry_variance > -0.000000001:
            dry_variance = 0.0

        dry_stddev = math.sqrt(dry_variance)
    else:
        dry_mean = ""
        dry_stddev = ""

    if wind_count > 0:
        wind_mean = wind_sum / wind_count
    else:
        wind_mean = ""

    print(
        f"{date}\t"
        f"{dry_count}\t"
        f"{dry_min if dry_min is not None else ''}\t"
        f"{dry_max if dry_max is not None else ''}\t"
        f"{dry_mean if dry_mean != '' else ''}\t"
        f"{dry_stddev if dry_stddev != '' else ''}\t"
        f"{wind_count}\t"
        f"{wind_mean if wind_mean != '' else ''}\t"
        f"{wind_max if wind_max is not None else ''}"
    )

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        date, values = line.split("\t", 1)
        dry_str, wind_str = values.split(",", 1)
    except ValueError:
        continue

    if current_date is None:
        current_date = date

    if date != current_date:
        emit(current_date)
        reset()
        current_date = date

    if dry_str != "":
        dry = float(dry_str)
        dry_count += 1
        dry_sum += dry
        dry_sumsq += dry * dry
        dry_min = dry if dry_min is None else min(dry_min, dry)
        dry_max = dry if dry_max is None else max(dry_max, dry)

    if wind_str != "":
        wind = float(wind_str)
        wind_count += 1
        wind_sum += wind
        wind_max = wind if wind_max is None else max(wind_max, wind)

emit(current_date)
