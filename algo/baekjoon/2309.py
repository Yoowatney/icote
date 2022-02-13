#!/usr/bin/env python3

dwarf = [int(input()) for _ in range(9)]

total = sum(dwarf)
def find(dwarf):
    for i in range(9):
        for j in range(i + 1, 9):
            if (total - dwarf[i] - dwarf[j] == 100):
                dwarf[i] = 0
                dwarf[j] = 0
                return
find(dwarf)
dwarf.sort()
for i in dwarf[2::]:
    print(i)
