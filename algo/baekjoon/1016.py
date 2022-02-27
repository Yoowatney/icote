from time import time

# start_time = time()
# minn, maxx = map(int,input().split())
# a = [i**2 for i in range(2,int(maxx**0.5)+1)]
# num = [1] * (maxx-minn+1)
# for i in a:
#     n = minn//i*i
#     while(n < maxx+1):
#         if n - minn >= 0:
#             num[n-minn] = 0
#         n += i
# print(sum(num))
#
# end_time = time()
# print(end_time - start_time)

import math

min, max = map(int, input().split())

A = list(range(min, max+1))
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
        print("i : ",i)
        A[key * i] = 0
        # A[(key*i)-min]=0
print(len(set(A.values())) - 1)


# 10 11 12 13 14 15 16 17 18 19 20
# 10 11 13 14 15 17 19
