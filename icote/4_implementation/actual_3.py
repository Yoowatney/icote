#!/usr/bin/env python3
# 몇 번 더 풀어봐야함

import sys
from time import sleep

[x,y,d] = [1, 1, 'n'] # input


maps = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]
#  maps = [[0] * width for _ in range(height)]
#  for i in range(height): # create a map
#      maps[i] = list(map(int, input().split()))
real_maps = [[1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]]
count = 1
maps[y][x] = -1
while True:
    if (maps[y][x - 1] == 0 or maps[y][x + 1] == 0 or maps[y - 1][x] == 0 or maps[y + 1][x] == 0): # 육지가 있다면
        if (d == 'n'):
            nx = x - 1
            ny = y
            if maps[ny][nx] == 0:
                x = nx
                y = ny
                maps[y][x] = -1
                count += 1
            d = 'w'
        elif (d == 'e'):
            nx = x
            ny = y - 1
            if maps[ny][nx] == 0:
                x = nx
                y = ny
                maps[y][x] = -1
                count += 1
            d = 'n'
        elif (d == 'w'):
            nx = x
            ny = y + 1
            if maps[ny][nx] == 0:
                x = nx
                y = ny
                maps[y][x] = -1
                count += 1
            d = 's'
        elif (d == 's'):
            nx = x + 1
            ny = y
            if maps[ny][nx] == 0:
                x = nx
                y = ny
                maps[y][x] = -1
                count += 1
            d = 'e'
        print("if", x, y, d, count)
    else: # 육지가 없다면
        print("이제부터 else문", x, y, d)
        if (d == 'n'):
            nx = x
            ny = y + 1 # 뒤로 한칸
            if real_maps[ny][nx] == 1:
                break # 종료
            else:
                #  d = 'w'
                x = nx
                y = ny
        elif (d == 'e'):
            nx = x - 1
            ny = y
            if real_maps[ny][nx] == 1:
                break # 종료
            else:
                #  d = 'n'
                x = nx
                y = ny
        elif (d == 'w'):
            nx = x + 1
            ny = y
            if real_maps[ny][nx] == 1:
                break # 종료
            else:
                #  d = 's'
                x = nx
                y = ny
        elif (d == 's'):
            nx = x
            ny = y - 1
            if real_maps[ny][nx] == 1:
                break # 종료
            else:
                #  d = 'e'
                x = nx
                y = ny
        print("else", x, y, d, count)
print(count)
