#!/usr/bin/env python3
import sys

n = 0
sum_x = 0.0
sum_y = 0.0
sum_x2 = 0.0
sum_xy = 0.0

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

    n += 1
    sum_x += x
    sum_y += y
    sum_x2 += x * x
    sum_xy += x * y

denominator = (n * sum_x2) - (sum_x * sum_x)

if n == 0 or denominator == 0:
    print("model\tn\tsum_x\tsum_y\tsum_x2\tsum_xy\tslope_m\tintercept_b")
    print(f"dewpoint_to_drybulb\t{n}\t{sum_x}\t{sum_y}\t{sum_x2}\t{sum_xy}\tNA\tNA")
else:
    m = ((n * sum_xy) - (sum_x * sum_y)) / denominator
    b = (sum_y - (m * sum_x)) / n

    print("model\tn\tsum_x\tsum_y\tsum_x2\tsum_xy\tslope_m\tintercept_b")
    print(f"dewpoint_to_drybulb\t{n}\t{sum_x}\t{sum_y}\t{sum_x2}\t{sum_xy}\t{m}\t{b}")
