from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        cur_node = q.popleft()
        for link_node in g[cur_node]:
            if not visited[link_node]: # 모든 간선에 대해 비교함
                q.append(link_node)
                visited[link_node] = visited[cur_node] + 1
visited = [0] * (n + 1)
bfs(x)

temp = []
for i in range(1, n + 1):
    if visited[i] == k and i != x:
        temp.append(i)
temp.sort()

if temp:
    print(*temp, sep="\n")
else:
    print(-1)
