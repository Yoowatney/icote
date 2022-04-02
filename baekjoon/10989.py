import sys
input = sys.stdin.readline

n = [0] * 10001
for _ in range(int(input())):
    n[int(input())] += 1

for i in range(1, 10001):
    while n[i]:
        print(i)
        n[i] -= 1
