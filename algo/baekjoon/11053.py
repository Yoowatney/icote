import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    temp = []
    for j in range(i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if temp:
        dp[i] = max(temp) + 1
    else: dp[i] = 1

print(max(dp))
print("== arr ==")
print(arr)
print("== dp ==")
print(dp)

# print("== temp ==")
# print(temp)
