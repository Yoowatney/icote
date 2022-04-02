from pprint import pprint


l = [list(map(int, input().split())) for _ in range(8)]
dp = [[0] * 8 for _ in range(8)]

dp[0][0] = 9

for i in range(8):
    for j in range(8):
        if i == 0 and j >= 1:
            dp[i][j] = dp[i][j - 1] + l[i][j]
        if j == 0 and i >= 1:
            dp[i][j] = dp[i - 1][j] + l[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + l[i][j]

pprint(dp)
# pprint(l)
