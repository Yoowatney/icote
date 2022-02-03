#!/usr/bin/env python3
from random import randint
import time
#  import itertools
#  chars = ['A', 'B', 'C']
#  p = list(itertools.permutations(chars, 2))
#
#  print(p)

#  for i in range(0, 3):
#      print(i)

#  c = "Hello"
#  if 'H' in c:
#      print("H in c")

#  a = str(60) + str(59)
#
#  if '6' in a:
#      print("6 in a")

#  a = [1, 1, 2, 3, 1]# [1 : 3] 1부터 2까지 인덱스 처리, range와 동일
#
#  a.remove(1)
#  print(a)

#  data = dict()
#  data['a'] = 1
#  data['b'] = 2
#  data['c'] = 3
#
#
#  for i in data:
#      print(i)


#  a = [3, 2, 5, 4, 1]

#  a = []
#  for _ in range(0, 10000):
#      a.append(randint(0, 10000))
#
#  start_time = time.time()
#
#  for i in range(0, len(a)):
#      for j in range(i, len(a)):
#          if a[i] > a[j] :
#              a[i], a[j] = a[j], a[i]
#
#  end_time = time.time()
#
#  print("my : ", end_time - start_time)
#
#
#  a = []
#  for _ in range(0, 10000):
#      a.append(randint(0, 10000))
#
#  start_time = time.time()
#
#  a.sort()
#
#  end_time = time.time()
#
#  print("in : ", end_time - start_time)

#  a = 'a1'
#  b = a[1]
#  print(type(b))

#  a = ord('1')
#  print(a)
#  a = 6
#  if 0 < a < 5:
#      print("a is in range")

#  from collections import deque
#
#  queue = deque([1,2])
#  print("queue", queue)
#  data = queue.popleft()
#
#  print("queue", queue)
#  print(data)

i = 0
while (i < i + 1):
    time.sleep(1)
    i = i + 1
    print(i)
