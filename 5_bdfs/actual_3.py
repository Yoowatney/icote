#!/usr/bin/env python3

from collections import deque
import sys

#  n, m = map(int, sys.stdin.readline().split())
#
#  for i in range(n):

n, m = 4, 5

def dfs(graph, row, col, visited):
    global n,m
    if (visited[row][col]):
        return (0)
    visited[row][col] = 1
    #  if (row + 1 >= n or col + 1 >= m):
    #      return (0)
    #  if (row + 1 >= n or col + 1 >= m):
    #      return (0)
    if (row + 1 < n and not visited[row + 1][col]):
        dfs(graph, row + 1, col, visited)
    if (col + 1 < m and not visited[row][col + 1]):
        dfs(graph, row, col + 1, visited)
    return (1) # not visited[row][col], row + 1 >=n or visited[row + 1][col]
    if (row + 1 < n and col + 1 < m):
        if (not visited[row + 1][col] or not visited[row][col + 1]):
            dfs(graph, row + 1, col, visited)
            dfs(graph, row, col + 1, visited)
            return (1)
    return (1) # not visited[row][col], visited[row + 1][col] and visited[row][col + 1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] 
def bfs(graph, row, col, visited):
    if (visited[row][col]):
        return (0)
    queue = deque()
    queue.append([row, col])
    while (queue):
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0):
                queue.append([nx, ny])
                visited[nx][ny] = 1
        # bfs 저질 구현
        #  if (pop_row + 1 < n and not visited[pop_row + 1][pop_col]):
        #      queue.append([pop_row + 1, pop_col])
        #      visited[pop_row + 1][pop_col] = 1
        #  if (pop_row - 1 >= 0 and not visited[pop_row - 1][pop_col]):
        #      queue.append([pop_row - 1, pop_col])
        #      visited[pop_row - 1][pop_col] = 1
        #  if (pop_col + 1 < m and not visited[pop_row][pop_col + 1]):
        #      queue.append([pop_row, pop_col + 1])
        #      visited[pop_row][pop_col + 1] = 1
        #  if (pop_col - 1 >= 0 and not visited[pop_row][pop_col - 1]):
        #      queue.append([pop_row, pop_col - 1])
        #      visited[pop_row][pop_col - 1] = 1
    return (1)

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0]
]
visited = graph

def dfs_other(x, y):
    if (x <= -1 or x >=n or y <= -1 or y >= m):
        return (0)
    if visited[x][y] == 1:
        return (0)
    visited[x][y] = 1
    dfs_other(x - 1, y)
    dfs_other(x + 1, y)
    dfs_other(x, y - 1)
    dfs_other(x, y + 1)
    return (1)

count = 0

for row in range(n):
    for col in range(m):
        #  count += dfs_other(row, col)

        if (bfs(graph, row, col, visited)):
            print(row, col)
        #  if (dfs(graph, row, col, visited)):
        #      count += 1
        #      print(row, col)
print(count)

#  for i in range(2):
#      data.append(list(map(int, input().split())))
#  print(data)

# for 2 array


