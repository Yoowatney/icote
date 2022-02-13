#!/usr/bin/env python3

n, m = map(int, input().split())

def getGCD(n,m):
    val = max(n,m)
    ret = 0
    for i in range(1, val + 1):
        if (n % i == 0 and m % i == 0):
            ret = max(ret, i)
    return ret

ret = getGCD(n, m)
print(ret)
print(n // ret * m // ret * ret)
