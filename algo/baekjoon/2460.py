#!/usr/bin/env python3

arr = []
for _ in range(10):
    a, b = list(map(int, input().split(' ')))
    arr.append(b - a)
max_val = 0
temp = 0
for val in arr:
    temp += val
    max_val = max(max_val, temp)
print(max_val)


# arr = [list(map(int, input().split(' '))) for _ in range(10)]
# arr = [map(int, input().split(' ')) for _ in range(10)]
# pprint(arr)
