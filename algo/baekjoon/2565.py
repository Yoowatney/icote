n = int(input())
arr = []
dp = [1] * n

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in range(n):
    temp = []
    for j in range(i):
        if arr[j][0] < arr[i][0] and arr[j][1] < arr[i][1]:
            temp.append(dp[j])
    if temp:
        dp[i] = max(temp) + 1
print(n - max(dp))
