import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, k = map(int, input().split())

g = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(current_node):
    if visited[current_node]:
        return 0
    visited[current_node] = True
    for link_node in g[current_node]:
        if not visited[link_node]:
            dfs(link_node)
    return 1

def bfs(i):
    if visited[i]:
        return 0
    visited[i] = True
    q = deque()
    q.append(i)
    while q:
        current_node = q.popleft()
        for link_node in g[current_node]:
            if not visited[link_node]:
                q.append(link_node)
                visited[link_node] = True
    return 1

count = 0
for current_node in range(1, n + 1):
    count += dfs(current_node)
    # count += bfs(current_node)
print(count)
    # if (dfs(current_node)):
    #     print(current_node)
    # count += dfs(current_node)
# print(count)
