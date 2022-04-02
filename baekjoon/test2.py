# a = [
#     [0, 1],
#     [2, 3],
#     [4, 5],
#     [6, 7],
#     [8, 9],
#
#
# print(*a)
#
# print(zip(*a))
from itertools import permutations

print(*permutations([1,2,3], 3))
# import sys
#
# print(int(sys.stdin.readline()))
# l = [1, 2, 3, 5, 8, 22, 34, 55]
# for index in range(0, len(l), 3):
#     print(l, l[index])

# def lower_bound(arr, num):
#     x = 0
#     upper = len(arr)
#     while x < upper:
#         mid = (x + upper) // 2
#         if arr[mid] < num:
#             x = mid + 1
#         else: # num <= mid
#             upper = mid
#     return x
#
# def upper_bound(arr, num):
#     x = 0
#     upper = len(arr)
#     while x < upper:
#         mid = (x + upper) // 2
#         if arr[mid] <= num:
#             x = mid + 1
#         else: # num < mid
#             upper = mid
#     return x
#
# print(format(1.5, '.0f'))
#
# print(round(4.6, 0))
#
# print(int(4.1 + 0.5))

# print(lower_bound([1,2,3,3,3,4], 3))
# print(upper_bound([1,2,3,3,3,4], 3))
# print(sorted(l, key=lambda l:l.items()))

# from collections import deque
#
# b = [0] * 5
# b[3] = 1
# l = deque(zip(map(int, input().split()), b))
#
# print(l)

# _,a = map(int, input().split())
# print(a)
# print(*zip([1,2],[2,3],[3,4]))
# prime_square = set()
#
# num = 10 ** 12
# prime_list = [False, False] + [True] * num 
#
# for i in range(2, int(num ** (1/2))): # 1000000 when mx = 10^12
#     if prime_list[i]:
#         for k in range(i * 2, num, i):
#             prime_list[k] = False
#
# prime_square = [i * i for i in prime_list]
# print(len(prime_square))

# for i in range(2, 10 ** 12 + 1):
#     if prime_list[i]: #and i * i <= mx:
#         prime_square.add(i * i)
#     elif i * i > num:
#         break

# def isPrime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# def isPrime(n):
#     for i in range(2, int(n ** 1/2)):
#         if n % i == 0:
#             return False
#     return True
#
# primes = list()
# for num in range(2, 100):
#     sign = 0
#     for i in range(2, num):
#         if num % i == 0:
#             sign = 1
#             break
#     if not sign:
#         primes.append(num)
# print(primes)
#
#
# primes = [False, False] + [True] * 100
# for num in range(2, 100):
#     for i in range(num * 2, 100, num):
#         primes[i] = False
# ret = [i for i in range(1, 100) if primes[i]]
# print(ret)
#
# from time import time
# import math
#
# n = 10
# start_time = time()
# primes = [False, False] + [True] * n
# for num in range(2, int(n ** 1/2) + 1):
#     for i in range(num * 2, n, num):
#         primes[i] = False
# ret = [i for i in range(1, n) if primes[i]]
# end_time = time()
# print(end_time - start_time)

# start_time = time()
# primes = [False, False] + [True] * n
# for num in range(2, int(n ** 1/2) + 1):
#     if primes[num]:
#         for i in range(num * 2, n, num):
#             primes[i] = False
# ret = [i for i in range(1, n) if primes[i]]
# end_time = time()
# print(end_time - start_time)
#
# start_time = time()
# primes = [False, False] + [True] * n
# for num in range(2, int(math.sqrt(n)) + 1):
#     if primes[num]:
#         for i in range(num * 2, n, num):
#             primes[i] = False
# ret = [i for i in range(1, n) if primes[i]]
# end_time = time()
# print(end_time - start_time)
#
#
# start_time = time()
# arr = [True] * (n + 1)
# for i in range(2, int(math.sqrt(n) + 1)):
#     if arr[i]:
#         j = 2
#         while i * j <= n:
#             arr[i * j] = False
#             j += 1
# ret = [i for i in range(2, n) if arr[i]]
# end_time = time()
# print(end_time - start_time)

