#!/usr/bin/env python3

# for _ in range(int(input())):
#     a = [i for i in str(input())]
#     print(a)

cnt = 0
def dfs(i, j, m):
    if (not (0 <= j < n) or not (0 <= i < n) or m[i][j] != 1):
        return 0
    global cnt

    m[i][j] = -1
    cnt += 1
    dfs(i + 1, j, m)
    dfs(i - 1, j, m)
    dfs(i, j + 1, m)
    dfs(i, j - 1, m)
    return 1

# cnt : 단지에 속하는 집 수 count
# count : 단지 개수
n = int(input())
m = [list(map(int, input())) for _ in range(n)]

count = 0
a = []
for i in range(0, n):
    for j in range(0, n):
        if (dfs(i, j, m)):
            count += 1
            a.append(cnt)
            cnt = 0
a.sort()
print(count, *a, sep="\n")

# arr = [list(map(int, input().split())) for _ in range(3)]
# print(arr)
