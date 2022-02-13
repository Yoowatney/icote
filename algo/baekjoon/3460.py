#!/usr/bin/env python3

t = int(input())

for _ in range(t):
    n = int(input())
    idx = 0
    num_list = []
    while (n):
        if (n % 2 == 1):
            num_list.append(idx)
        n = n >> 1
        idx += 1
    print(*num_list)
