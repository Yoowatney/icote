import sys
input = sys.stdin.readline

n = int(input())
m = sorted(list(map(int ,input().split())))

if len(m) > 1:
    print(m[0] * m[-1])
else:
    print(m[0] ** 2)



