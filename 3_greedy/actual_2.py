#!/usr/bin/env python3

import sys

N, M, K= map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# N : 배열의 크기
# M : 횟수
# K : 반복 최대 횟수
# array : 배열

maxValue = sorted(array, reverse=True)[0]
secondMaxValue = sorted(array, reverse=True)[1]

# 5 7 2
ret = (M % (K + 1)) * maxValue  # 4 * 1 = 4
if (M == K):
    form = maxValue * K
else:
    form = maxValue * K + secondMaxValue # form = 4 * 2 + 4 = 12
ret = (M // (K + 1)) * form + ret # 7 // 2 = 3 , 3 * 12 + 4 = 40

print("ret", ret)
