#!/usr/bin/env python3
import sys
import math

current_station = None

dry_count = 0
dry_sum = 0.0
dry_sumsq = 0.0
dry_min = None
dry_max = None

wind_count = 0
wind_sum = 0.0
wind_sumsq = 0.0
wind_min = None
wind_max = None

def reset():
    global dry_count, dry_sum, dry_sumsq, dry_min, dry_max
    global wind_count, wind_sum, wind_sumsq, wind_min, wind_max

    dry_count = 0
    dry_sum = 0.0
    dry_sumsq = 0.0
    dry_min = None
    dry_max = None

    wind_count = 0
    wind_sum = 0.0
    wind_sumsq = 0.0
    wind_min = None
    wind_max = None

def compute_stats(count, total, sumsq, min_val, max_val):
    if count == 0:
        return "", "", "", "", ""

    mean = total / count
    variance = (sumsq / count) - (mean * mean)

    if variance < 0 and variance > -0.000000001:
        variance = 0.0

    stddev = math.sqrt(variance)

    return mean, variance, stddev, min_val, max_val

def emit(station):
    if station is None:
        return

    dry_mean, dry_var, dry_std, dry_min_out, dry_max_out = compute_stats(
        dry_count, dry_sum, dry_sumsq, dry_min, dry_max
    )

    wind_mean, wind_var, wind_std, wind_min_out, wind_max_out = compute_stats(
        wind_count, wind_sum, wind_sumsq, wind_min, wind_max
    )

    print(
        f"{station}\t"
        f"{dry_count}\t{dry_mean}\t{dry_var}\t{dry_std}\t{dry_min_out}\t{dry_max_out}\t"
        f"{wind_count}\t{wind_mean}\t{wind_var}\t{wind_std}\t{wind_min_out}\t{wind_max_out}"
    )

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        station, values = line.split("\t", 1)
        dry_str, wind_str = values.split(",", 1)
    except ValueError:
        continue

    if current_station is None:
        current_station = station

    if station != current_station:
        emit(current_station)
        reset()
        current_station = station

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
        wind_sumsq += wind * wind
        wind_min = wind if wind_min is None else min(wind_min, wind)
        wind_max = wind if wind_max is None else max(wind_max, wind)

emit(current_station)
