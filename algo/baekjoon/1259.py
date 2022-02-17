#!/usr/bin/env python3

def process():
    a = input()
    if (a == "0"): raise Exception("!")
    if (a[::-1] == a): return "yes"
    return "no"
try:
    while (1):
        print(process())
except:
    pass
