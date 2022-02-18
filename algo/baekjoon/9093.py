#!/usr/bin/env python3

def reverseWord():
    n = input().split()
    for i in range(len(n)):
        n[i] = n[i][::-1]
    return (n)
for _ in range(int(input())):
    print(*reverseWord())
