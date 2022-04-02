#!/usr/bin/env python3

from itertools import permutations

int(input())
num_list = list(map(int, input().split()))
oper = list(map(int, input().split()))
permutes = list(permutations(num_list))

oper.insert(0, 1)
print(permutes)
print(oper)

for _list in permutes:
    e, a, b, c, d = oper
    val = 0
    for i in _list:
        if (e == 1):
            e -= 1
            val = i
        elif a:
            a -= 1
            val += i
        elif b:
            b -= 1
            val -= i
        elif c:
            c -= 1
            val *= i
        elif d:
            d -= 1
            if (val < 0):
                val -= 1
                val //= i
            else:
                val //= i
        print("val", val, "i", i)
    print("")
