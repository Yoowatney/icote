import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    temp = []
    for j in range(i):
        if arr[j] > arr[i]:
            temp.append(dp[j] + 1)
    if temp:
        dp[i] = max(temp)
print(max(dp))
print(arr)
print(dp)
