from collections import deque
import sys

input = sys.stdin.readline
n,m,k = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m): # 인접리스트 선택
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n + 1):
    g[i].sort()
visited = [False] * (n + 1)

def bfs(cur): 
    q = deque()
    q.append(cur)
    while q:
        cur_node = q.popleft()
        print(cur_node, end=" ")
        visited[cur_node] = True
        for link_node in g[cur_node]:
            if visited[link_node]:
                continue
            q.append(link_node)
            visited[link_node] = True

def dfs(cur_node):
    visited[cur_node] = True
    print(cur_node, end=" ")
    for link_node in g[cur_node]:
        if not visited[link_node]:
            dfs(link_node)

dfs(k)
visited = [False] * (n + 1)
print()
bfs(k)
