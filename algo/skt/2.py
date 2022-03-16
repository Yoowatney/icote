
from collections import deque

def solution(n, clockwise):
    result = [[0] * n for _ in range(n)]
    if n % 2 != 0:
        temp = list(range(n - 1, 1, -2))
    else:
        temp = list(range(n - 1, 2, -2))
    l = [[0,0], [n - 1, 0], [n - 1, n - 1], [0, n - 1]]
    rotation = 0 # 각 소용돌이마다 방향을 바꿈
    num = 0 # 채울 숫자
    for x, y in l: # 소용돌이 네 방향 시작 좌표
        num = 1
        ways = deque()
        ways.append([1, 0])
        ways.append([0, 1])
        ways.append([-1, 0])
        ways.append([0, -1])
        ways.rotate(rotation)
        for number in temp:
            dx, dy = ways.popleft()
            ways.append([dx, dy])
            for _ in range(0, number):
                if num != 1:
                    x += dx
                    y += dy
                result[y][x] = num
                num += 1
        rotation -= 1 # 한 소용돌이마다 도는 방향이 다름
    # 마지막 칸 채우기
    c = n // 2 # 기준 좌표
    if n % 2 != 0:
        result[c][c] = num
    else:
        for x,y in [[c - 1, c - 1],[c - 1, c], [c, c - 1], [c, c]]: 
            result[x][y] = num

    if not clockwise: # clockwise가 아니면 swap
        for i in range(0, n):
            temp = -1
            for j in range(0, n // 2):
                result[i][j], result[i][temp] = result[i][temp], result[i][j]
                temp -= 1
    return result
from pprint import pprint
pprint(solution(9, False))
