from pprint import pprint
from copy import deepcopy
from itertools import combinations
from collections import deque

ways = [[1, 0], [-1, 0], [0, 1], [0, -1]]

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]


count = 1
visited = [[False] * m for _ in range(n)]

l = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        l.append([i, j])

def bfs(y, x, a, b, c):
    global copy_g
    global copy_visited
    q = deque()
    q.append([x,y])

    copy_visited[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()
        for way_x, way_y in ways:
            link_x = way_x + cur_x
            link_y = way_y + cur_y
            if 0 <= link_x < m and 0 <= link_y < n and not copy_visited[link_y][link_x] and copy_g[link_y][link_x] == 0:
                q.append([link_x, link_y])
                copy_visited[link_y][link_x] = True
                copy_g[link_y][link_x] = 2

_max = 0
for a,b,c in combinations(l, 3): # 40000
    copy_g = deepcopy(g)
    copy_visited = deepcopy(visited)
    if copy_g[a[0] - 1][a[1] - 1] == 0 and copy_g[b[0] - 1][b[1] - 1] == 0 and copy_g[c[0] - 1][c[1] - 1] == 0:
        copy_g[a[0] - 1][a[1] - 1] = 1
        copy_g[b[0] - 1][b[1] - 1] = 1
        copy_g[c[0] - 1][c[1] - 1] = 1
    else:
        continue
    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                bfs(i, j, a, b, c)
    count = 0
    for i in range(n):
        for j in range(m):
            if copy_g[i][j] == 0:
                count += 1
    _max = max(count, _max)
print(_max)
