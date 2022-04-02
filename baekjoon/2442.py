#!/usr/bin/env python3

n = int(input())
for i in range(0, n):
    print(('*' * (2 * i + 1)).center(2 * n - 1)[:i + n])
