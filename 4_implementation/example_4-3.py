#!/usr/bin/env python3

# input 

val = input()

x = ord(val[0]) - 96
y = int(val[1])

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        count += 1
print(count)
