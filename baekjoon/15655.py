from itertools import combinations
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

for ret in combinations(arr, m):
    print(*ret)
