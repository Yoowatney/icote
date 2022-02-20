from pprint import pprint
from copy import deepcopy

def dfs(y, x):
    if not 0 <= x < w or not 0 <= y < h or visited[y][x] or g[y][x] != 1:
        return 0
    visited[y][x] = 1
    dfs(y + 1, x)
    dfs(y - 1, x)
    dfs(y, x + 1)
    dfs(y, x - 1)
    return 1

    
for _ in range(int(input())):
    # g = make_array()
    w, h, k = map(int, input().split())
    g = [[0] * w for _ in range(h)]
    visited = deepcopy(g)
    for _ in range(k):
        x, y = map(int, input().split()) # 시간 초과시 sys
        g[y][x] = 1
    count = 0
    for i in range(h):
        for j in range(w):
            count += dfs(i, j)
    pprint(g)
    print(count)

