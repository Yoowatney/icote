#!/usr/bin/env python3

import sys

#  n = int(input())
n = 5

plan = list(input().split())

x, y = [1, 1]

for i in plan:
    if (i == 'U' and x > 1):
        x -= 1
    elif (i == 'D' and x < n):
        x += 1
    elif (i == 'L' and y > 1):
        y -= 1
    elif (i == 'R' and y < n):
        y += 1
print(x, y)
