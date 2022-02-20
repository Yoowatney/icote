#!/usr/bin/env python3

# from sys import stdin
# from pprint import pprint
from collections import deque

# def dfs(g, n, visited):
#     if visited[n]:
#         return
#     visited[n] = True
#     global count
#     count += 1
#     for i in g[n]:
#         dfs(g, i, visited)
#
n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(int(input())):
    i, val = map(int, input().split())
    g[i].append(val)
    g[val].append(i)

count = 0
distance = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs(g, n, visited):
    visited[n] = True 
    distance[n] = 0 # list는 전역변수 선언 안해도 됨?
    q = deque([n])
    count = 0
    while (q):
        val = q.popleft() # 이름 명명 뭐로하면 좋을지.. cur_node
        count += 1
        for i in g[val]: # 이름 명명 뭐로하면 좋을지.. link_node
            if not visited[i]: # 이름 명명 뭐로하면 좋을지..
                q.append(i)
                visited[i] = True
    return count

# def bfs(g, n, visited): # global쓰지말고 다시 푸세용!
#     visited[n] = True
#     dq = deque([n])
#     global count
#     while (dq):
#         i = dq.popleft()
#         count += 1
#         for val in g[i]:
#             if (not visited[val]):
#                 visited[val] = True
#                 dq.append(val)
# dfs(g, 1, visited)
# print(visited.count(True) - 1)

print(bfs(g, 1, visited) - 1)


# n = int(input()) # 컴퓨터의 수
# m = int(input()) # 연결된 수
#
# graph = [[0] * (n+1) for _ in range(n+1)] # 인접행렬 생성
#
# for _ in range(m):
#     x, y = map(int, stdin.readline().split())
#     graph[x][y] = 1
#     graph[y][x] = 1
#
# visited = [False] * (n + 1)
#
# def dfs(graph, n, visited):
#     if (visited[n]):
#         return
#     visited[n] = True
#     global count
#     count += 1
#     for i in range(len(graph[n])):
#         if (graph[n][i] == 1):
#             dfs(graph, i, visited)
# count = 0
# dfs(graph, 1, visited)
#
# print(visited)
# pprint(graph)
# print(count - 1)
