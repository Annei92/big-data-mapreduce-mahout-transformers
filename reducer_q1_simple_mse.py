#!/usr/bin/env python3
import sys
import math

count = 0
sum_squared_error = 0.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, value = line.split("\t", 1)
        squared_error = float(value)
    except ValueError:
        continue

    count += 1
    sum_squared_error += squared_error

if count == 0:
    print("model\tn\tsum_squared_error\tmse\trmse")
    print("dewpoint_to_drybulb\t0\tNA\tNA\tNA")
else:
    mse = sum_squared_error / count
    rmse = math.sqrt(mse)

    print("model\tn\tsum_squared_error\tmse\trmse")
    print(f"dewpoint_to_drybulb\t{count}\t{sum_squared_error}\t{mse}\t{rmse}")
