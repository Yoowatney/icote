import sys
from collections import deque


# sys.setrecursionlimit(10000)
# from pprint import pprint
# from copy import deepcopy
# from time import sleep


input = sys.stdin.readline

# def dfs(y, x):
#     if not 0 <= x < w or not 0 <= y < h or visited[y][x] or g[y][x] != 1:
#         return 0
#     visited[y][x] = 1
#     dfs(y + 1, x)
#     dfs(y - 1, x)
#     dfs(y, x + 1)
#     dfs(y, x - 1)
#     return 1

def bfs(y, x):
    g[y][x] = 0
    q = deque()
    q.append((y,x))
    while q:
        cur_y, cur_x = q.popleft()
        for way in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = cur_x + way[1]
            ny = cur_y + way[0]
            if (0 <= nx < w and 0 <= ny < h and g[ny][nx] == 1):
                q.append((cur_y + way[0], cur_x + way[1]))
                g[ny][nx] = 0

for _ in range(int(input())):
    # g = make_array()
    w, h, k = map(int, input().split())
    g = [[0] * w for _ in range(h)]
    # visited = deepcopy(g)
    for _ in range(k):
        x, y = map(int, input().split()) # 시간 초과시 sys
        g[y][x] = 1
    count = 0
    for i in range(h):
        for j in range(w):
            if (g[i][j] == 1):
                count += 1
                bfs(i, j)
            # count += dfs(i, j)
    print(count)
