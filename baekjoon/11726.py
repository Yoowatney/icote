dp = [-1, 1, 2] + [-1] * 1001
for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[int(input())] % 10007)
