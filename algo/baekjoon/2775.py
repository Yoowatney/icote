import sys
input = sys.stdin.readline

a = [[0] * 14 for _ in range(15)]

a[0] = list(range(1,15))

for h in range(1, 15):
    for w in range(14):
        a[h][w] = sum(a[h - 1][:w + 1])

for _ in range(int(input())):
    print(a[int(input())][int(input()) - 1])
