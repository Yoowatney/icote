#!/usr/bin/env python3

#  a = 3
#
#  b = a
#
#  a = 5
#  print("a", a)
#  print("b", b)

from collections import deque

queue = deque()

a = 1
b = 2
queue.append([a,b])

print(queue)
print(queue.popleft())
