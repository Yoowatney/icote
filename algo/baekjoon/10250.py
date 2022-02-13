#!/usr/bin/env python3

import sys
t = int(input())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    floor = n % h
    room = n // h + 1
    if (floor == 0):
        floor = h
        room = room - 1
    print(str(floor) + '0' + str(room) if room < 10 else str(floor) + str(room))
