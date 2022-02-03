#!/usr/bin/env python3

#  from collections import deque

#  import deque
#
#  queue = deque()
#
#  print(queue)


#  stdin = "Hello!"
#  print(stdin)
#  from sys import stdin
#  data = stdin.readline().rstrip()

#  print(stdin)
#  print(dir(sys))

#  print(collections.deque())


#  stack = []
#
#  stack.append((1, 2))
#  stack.append(2)
#  stack.append(3)
#  print(stack[0][0])


from collections import deque
from time import sleep

#  queue = deque()
#  if (queue):
#      print("Queue is not empty")
#  else:
#      print("Queue is empty")
#  queue.append(1)
#  queue.append(2)
#  queue.append(3)
#  queue.popleft()
#


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#  def bfs(graph, v, visited):
#      visited[v] = True
#      print(v, end=' ')
#      queue = deque([v])
#      while queue:
#          v = queue.popleft()
#          for i in graph[v]:
#              if not visited[i]:
#                  queue.append(i)
#                  visited[i] = True
#                  print(i, end=' ')

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while (queue):
        node = queue.popleft()
        print(node,end=" ")
        for i in graph[node]:
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
    [2,6,8],
    [1,7]
]

visited = [False] * 9
#  dfs(graph, 1, visited)

print("\n")

visited = [False] * 9
bfs(graph, 1, visited)
