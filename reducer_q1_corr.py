#!/usr/bin/env python3
import sys
import math

current_key = None

n = 0
sum_x = 0.0
sum_y = 0.0
sum_x2 = 0.0
sum_y2 = 0.0
sum_xy = 0.0

def reset():
    global n, sum_x, sum_y, sum_x2, sum_y2, sum_xy
    n = 0
    sum_x = 0.0
    sum_y = 0.0
    sum_x2 = 0.0
    sum_y2 = 0.0
    sum_xy = 0.0

def strength_label(corr):
    abs_corr = abs(corr)

    if abs_corr >= 0.7:
        return "strong"
    elif abs_corr >= 0.3:
        return "moderate"
    else:
        return "weak"

def emit(key):
    if key is None or n == 0:
        return

    mean_x = sum_x / n
    mean_y = sum_y / n

    var_x = (sum_x2 / n) - (mean_x * mean_x)
    var_y = (sum_y2 / n) - (mean_y * mean_y)
    covariance = (sum_xy / n) - (mean_x * mean_y)

    # Avoid tiny negative variance caused by floating-point precision.
    if var_x < 0 and var_x > -1e-9:
        var_x = 0.0

    if var_y < 0 and var_y > -1e-9:
        var_y = 0.0

    if var_x == 0.0 or var_y == 0.0:
        correlation = 0.0
    else:
        correlation = covariance / math.sqrt(var_x * var_y)

    if correlation > 0:
        direction = "positive"
    elif correlation < 0:
        direction = "negative"
    else:
        direction = "none"

    strength = strength_label(correlation)

    print(
        f"{key}\t"
        f"{n}\t"
        f"{mean_x}\t"
        f"{mean_y}\t"
        f"{covariance}\t"
        f"{correlation}\t"
        f"{direction}\t"
        f"{strength}"
    )

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)
        x_str, y_str = values.split(",", 1)
        x = float(x_str)
        y = float(y_str)
    except ValueError:
        continue

    if current_key is None:
        current_key = key

    if key != current_key:
        emit(current_key)
        reset()
        current_key = key

    n += 1
    sum_x += x
    sum_y += y
    sum_x2 += x * x
    sum_y2 += y * y
    sum_xy += x * y

emit(current_key)
