#!/usr/bin/env python3

import sys

while (True):
    x,y,z = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    if (x == 0):
        break
    if (x**2 + y**2 == z**2):
        print("right")
    else:
        print("wrong")
