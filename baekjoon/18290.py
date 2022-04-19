from itertools import combinations
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

comb = []

for i in range(n):
    for j in range(m):
        comb.append([i, j])

total = -9e10
for ret in combinations(comb, k):
    signed = False
    for [[r1, c1], [r2, c2]] in combinations(ret, 2):
        if abs(r1 - r2) + abs(c1 - c2) == 1:
            break
    else:
        signed = True
    if not signed:
        continue
    total = max(total, sum(arr[r][c] for r, c in ret))
print(total)

# def check(elem, ret):
#     for dx, dy in zip(dxs, dys):
#         nx = dx + elem[0]
#         ny = dy + elem[1]
#         if [nx, ny] in ret:
#             return False
#     return True
#
# def get_value(elems):
#     ret = 0
#     for i in elems:
#         ret += arr[i[0]][i[1]]
#     return ret

# import itertools
# n,m,k=map(int,input().split())
# arr=[list(map(int,input().split())) for _ in range(n)]
# index=[i for i in range(n*m)]
# coms=itertools.combinations(index,k)
# res=-1e9
# for com in coms:
#     s=0
#     check=set()
#     dekiru=True
#     for idx in com:
#         r=idx//m
#         c=idx%m
#         if [r-1, c] in com or [r+1, c] in com or [r, c-1] in com or [r, c+1] in com:
#             dekiru=False
#             break
#         s+=arr[r][c]
#         check.add((r,c))
#     if dekiru:
#         res=max(res,s)
# print(res)


# import itertools
# n,m,k=map(int,input().split())
# arr=[list(map(int,input().split())) for _ in range(n)]
# index=[i for i in range(n*m)]
# coms=itertools.combinations(index,k)
# res=-1e9
# for com in coms:
#     s=0
#     check=set()
#     dekiru=True
#     for idx in com:
#         r=idx//m
#         c=idx%m
#         if (r-1, c)in check or (r+1, c)in check or (r, c-1)in check or (r, c+1) in check:
#             dekiru=False
#             break
#         s+=arr[r][c]
#         check.add((r,c))
#     if dekiru:
#         res=max(res,s)
# print(res)
