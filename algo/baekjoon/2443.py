#!/usr/bin/env python3

n = int(input())
for i in range(n, 0, -1):
    print(('*' * (2 * i - 1)).center(2 * n - 1)[:i + n])

