#!/usr/bin/env python3
from collections import deque
from pprint import pprint
import copy

n = 5
m = 6

array = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
        ]
able_to_go = copy.deepcopy(array)

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

def bfs(array):
    q = deque()
    q.append((0, 0))
    able_to_go[0][0] = 0
    array[0][0] = 1
    while (q):
        y,x = q.popleft()
        print(y, x)
        able_to_go[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 있는 조건 만들어주기
            if (0 <= nx < m and 0 <= ny < n and able_to_go[ny][nx] == 1):
                q.append((ny, nx))
                able_to_go[ny][nx] = 0
                array[ny][nx] = array[y][x] + 1
bfs(array)
pprint(array)
