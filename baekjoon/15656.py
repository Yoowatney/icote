from itertools import product

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

for ret in product(arr, repeat=m):
    print(*ret)
