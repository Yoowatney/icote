from collections import deque
import sys


n,m,k = map(int, input().split())

g = [[] for _ in range(n + 1)]

# for _ in range(m):
#     # a,b = map(int, input().split())
#     a,b = map(int, sys.stdin.readline().rstrip().split())
#     g[a].append(b)
#     g[b].append(a)
# for _ in range(n + 1):
#     g[_].sort()
# # for i in range(m): # 내부 정렬 어떻게하는게 좋음?
# #     g[i].sort
#
# def bfs():
#     visited[k] = True
#     q = deque([k])
#     # ret = []
#     while (q):
#         current_node = q.popleft()
#         print(current_node, end=' ')
#         # ret.append(current_node)
#         for link_node in g[current_node]:
#             if not visited[link_node]:
#                 q.append(link_node)
#                 visited[link_node] = True
#     # return ret
#
# dfs_ret = []
# def dfs(current_node):
#     visited[current_node] = True
#     dfs_ret.append(current_node)
#     for link_node in g[current_node]:
#         if not visited[link_node]:
#             dfs(link_node)
    
visited = [False] * (n + 1)
# dfs(k)
# print(*dfs_ret)
# visited = [False] * (n + 1)
# bfs()
# print(*bfs())
