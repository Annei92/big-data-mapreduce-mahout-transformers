#!/usr/bin/env python3
import sys

n = 0

sum_x1 = 0.0
sum_x2 = 0.0
sum_y = 0.0

sum_x1x1 = 0.0
sum_x2x2 = 0.0
sum_x1x2 = 0.0

sum_x1y = 0.0
sum_x2y = 0.0

def determinant_3x3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        key, values = line.split("\t", 1)
        x1_str, x2_str, y_str = values.split(",", 2)
        x1 = float(x1_str)
        x2 = float(x2_str)
        y = float(y_str)
    except ValueError:
        continue

    n += 1

    sum_x1 += x1
    sum_x2 += x2
    sum_y += y

    sum_x1x1 += x1 * x1
    sum_x2x2 += x2 * x2
    sum_x1x2 += x1 * x2

    sum_x1y += x1 * y
    sum_x2y += x2 * y

# Normal equation matrix:
# [ n        sum_x1    sum_x2  ] [b0] = [sum_y]
# [ sum_x1   sum_x1x1  sum_x1x2] [b1] = [sum_x1y]
# [ sum_x2   sum_x1x2  sum_x2x2] [b2] = [sum_x2y]

A = [
    [n, sum_x1, sum_x2],
    [sum_x1, sum_x1x1, sum_x1x2],
    [sum_x2, sum_x1x2, sum_x2x2],
]

B = [sum_y, sum_x1y, sum_x2y]

det_A = determinant_3x3(A)

print("model\tn\tsum_x1_dewpoint\tsum_x2_humidity\tsum_y_drybulb\tsum_x1x1\tsum_x2x2\tsum_x1x2\tsum_x1y\tsum_x2y\tb0_intercept\tb1_dewpoint\tb2_humidity")

if n == 0 or det_A == 0:
    print(
        f"dewpoint_humidity_to_drybulb\t{n}\t"
        f"{sum_x1}\t{sum_x2}\t{sum_y}\t"
        f"{sum_x1x1}\t{sum_x2x2}\t{sum_x1x2}\t"
        f"{sum_x1y}\t{sum_x2y}\tNA\tNA\tNA"
    )
else:
    A_b0 = [
        [B[0], sum_x1, sum_x2],
        [B[1], sum_x1x1, sum_x1x2],
        [B[2], sum_x1x2, sum_x2x2],
    ]

    A_b1 = [
        [n, B[0], sum_x2],
        [sum_x1, B[1], sum_x1x2],
        [sum_x2, B[2], sum_x2x2],
    ]

    A_b2 = [
        [n, sum_x1, B[0]],
        [sum_x1, sum_x1x1, B[1]],
        [sum_x2, sum_x1x2, B[2]],
    ]

    b0 = determinant_3x3(A_b0) / det_A
    b1 = determinant_3x3(A_b1) / det_A
    b2 = determinant_3x3(A_b2) / det_A

    print(
        f"dewpoint_humidity_to_drybulb\t{n}\t"
        f"{sum_x1}\t{sum_x2}\t{sum_y}\t"
        f"{sum_x1x1}\t{sum_x2x2}\t{sum_x1x2}\t"
        f"{sum_x1y}\t{sum_x2y}\t"
        f"{b0}\t{b1}\t{b2}"
    )
