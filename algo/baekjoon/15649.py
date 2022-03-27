from itertools import permutations
n,m = map(int,input().split())
ret = permutations(range(1, n + 1), m)
for i in ret:
    print(*i)
