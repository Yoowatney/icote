import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

def dfs(v):
    for link_node in graph[v]:
        if not visited[link_node]:
            visited[link_node] = v
            dfs(link_node)

visited[1] = -1
dfs(1)
print(*visited[2:], sep="\n")













# print(graph)
# visited = [0]*(n+1)
#
# arr = []
#
# def dfs(s):
#     print(s)
#     print(visited)
#     for i in graph[s]:
#         if visited[i] == 0:
#             visited[i] = s
#             dfs(i)
#
# visited[1] = -1
# dfs(1)
#
# for x in range(2, n+1):
#     print(visited[x])
#
