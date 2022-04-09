from itertools import permutations

n, m = map(int, input().split())
arr = sorted(map(int,input().split()))
for ret in permutations(arr, m):
    print(*ret)
# print(arr)
# print(permutations)
# print(*combinations([1,7,8,9], 2))
# print(*permutations([7,1,8,9], 2))

