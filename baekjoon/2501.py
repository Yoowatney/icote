#!/usr/bin/env python3

n, k = map(int, input().split())

idx = 0
for i in range(1, n+1): # i는 약수값
    if (n % i == 0):
        idx += 1
    if (idx == k):
        print(i)
        break
    if (i == n):
        print(0)
