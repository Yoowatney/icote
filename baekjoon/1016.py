# from time import time
#
# import math

#
# min, max = map(int, input().split())
#
# A = dict()
# for i in range(min, max + 1):
#     A[i] = i
#
# def eratosthenes(n):
#     sieve = [True] * n
#     for i in range(2, n):
#         if sieve[i]:
#             a=2
#             while i*a < n:
#                 sieve[a*i] = False
#                 a += 1
#     result = []
#     for i in range(2, n):
#         if sieve[i] == True :
#             result.append(i)
#     return result
# n = math.floor(math.sqrt(max)) + 1 
# array = eratosthenes(n) 
#
# temp = 0
# for prime_number in array: # 8만개
#     key = prime_number**2
#     a = math.ceil(min/key)
#     b = max//key
#     for i in range(a, b+1): # 25만개
#         temp += 1
#         A[key * i] = 0
# print(len(set(A.values())) - 1)
# print(temp)

# 10 11 12 13 14 15 16 17 18 19 20
# 10 11 13 14 15 17 19
import math
mn, mx = map(int, input().split())

num = int(math.sqrt(mx)) + 1
a = [False, False] + [True] * num

temp = 0
for i in range(2, num):
    temp += 1
    if a[i]:
        for k in range(i * 2, num, i):
            temp += 1
            a[k] = False
prime_square = set()
for i in range(2, num):
    temp += 1
    if a[i] and i * i <= mx:
        prime_square.add(i * i)
    elif i * i > mx:
        break

square = set()

for num in prime_square: # 80000개
    left = mn // num - 1
    right = mx // num + 1
    for i in range(left, right):
        temp += 1
        if mn <= num * i <= mx:
            square.add(num * i)
total = mx - mn + 1
print(total - len(square))
print(temp)
