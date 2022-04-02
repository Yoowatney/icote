#!/usr/bin/env python3

import sys

n = int(input())

arr = []
for _ in range(n):
    # a, b = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    # arr.append([b, a])
    arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
# arr.sort()
arr.sort(key=lambda x:(x[0], x[1], -x[2]))
# arr.sort(key=lambda x:(x[1], x[0])) # y값 정렬
# for a,b,c in arr:
#     print(a, b)
for a,b,c in arr:
    print(a, b, c)
# print(arr)
