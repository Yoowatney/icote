# from itertools import permutations
# n,m = map(int,input().split())
# ret = permutations(range(1, n + 1), m)
# for i in ret:
#     print(*i)

# from collections import Counter

n,m = map(int,input().split())

arr = []
s = set()

def overlap():
    if len(s) < m:
        return True
    return False

def choose(num):
    if num == m + 1:
        print(*arr)
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        arr.append(i)
        s.add(i)
        choose(num + 1)
        arr.pop()
        s.remove(i)
choose(1)

