from time import time

import math

min, max = map(int, input().split())

A = dict()
for i in range(min, max + 1):
    A[i] = i
print(A)

def eratosthenes(n):
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i]:
            a=2
            while i*a < n:
                sieve[a*i] = False
                a += 1
    result = []
    for i in range(2, n):
        if sieve[i] == True :
            result.append(i)
    return result
n = math.floor(math.sqrt(max)) + 1 
array = eratosthenes(n) 
print(len(array))
for prime_number in array: # 8만개
    key = prime_number**2
    a = math.ceil(min/key)
    b = max//key
    for i in range(a, b+1): # 25만개
        A[key * i] = 0
print(len(set(A.values())) - 1)


# 10 11 12 13 14 15 16 17 18 19 20
# 10 11 13 14 15 17 19
