from itertools import combinations
import sys

input = sys.stdin.readline
i = 0
while True:
    n, *arr = map(int, input().split())
    if n == 0:
        break
    elif i != 0:
        print()
    i = 1
    ret = list(combinations(arr, 6))
    for val in ret:
        print(*val)
