#!/usr/bin/env python3

import sys


n, m = map(int, input().split())

print(n, m)

maxValue = 0
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    minValue = min(data)
    if (maxValue < minValue):
        maxValue = minValue
print(maxValue)
