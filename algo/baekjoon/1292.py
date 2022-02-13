#!/usr/bin/env python3

arr = []
for i in range(1, 46):
    for j in range(0, i):
        arr.append(i)
a, b = map(int, input().split())
print(sum(arr[a - 1 : b]))
