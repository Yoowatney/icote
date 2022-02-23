#!/usr/bin/env python3
import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
arr.sort()

for a,b in arr:
    print(a, b)


# for _ in range(n):
#     arr.append(list(map(int, input().split(' '))))

# a = [[3,4], [1, -2], [1,1], [1, -1], [2, 2], [3, 3]]
#
# a.sort()
# print(a)
