import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

total = 0
for i in range(n):
    if dp[i - 1] < 0:
        total = 0
    total += arr[i]
    dp[i] = total
print(max(dp))
print(dp)

from random import randint

a = []
for i in range(5):
    a.append(randint(-100, 100))
print(a)
exit(0)
