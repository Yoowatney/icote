#!/usr/bin/env python3

from collections import deque

#  def bfs(graph, v, visited):
#      queue = deque()
#      queue.append(v)
#      visited[v] = True
#      while queue:
#          node = queue.popleft()
#          print(node, end=' ')
#          for i in graph[node]:
#              if not visited[i]:
#                  queue.append(i)
#                  visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while (queue):
        now_pos = queue.popleft()
        print(now_pos,end=' ')
        for i in graph[now_pos]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9 # False * 9?

bfs(graph, 1, visited)

print()
visited = [False] * 9 # False * 9?
dfs(graph, 1, visited);
