#!/usr/bin/env python3

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

result = 0
while (True):
    target = (n // k) * k # target은 무조건 k의 배수
    print('target', target)
    result += (n - target)
    n = target # 따라서 n역시 k의 배수
    if n < k: # k의 배수가 k보다 작을 경우는 0뿐이다
        break 
    result += 1
    n //= k
print('n', n, 'result', result)
result += n - 1 # 고로 += 1로 바꿔줘도 되지않니..?
print(result)

#  count = 0
#  while (True):
#      if (n == 1):
#          break ;
#      if (n % k == 0):
#          n = n // k
#          count += 1
#      else:
#          n -= 1
#          count += 1
#
#  print("count", count)
