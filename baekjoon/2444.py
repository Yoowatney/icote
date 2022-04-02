#!/usr/bin/env python3

n = int(input())
for i in range(1, 2*n):
    print(('*' * (2*i - 1)).center(2*n - 1)[:n + i - 1]) if i <= n  else print(('*' * (4*n - 1 -2*i)).center(2*n - 1)[:3*n -i - 1])
    # print(a.center(2*n - 1)[:n + i - 1])
