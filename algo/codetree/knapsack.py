from pprint import pprint

weight = [0, 2, 6, 2, 3, 4]
price = [0, 3, 5, 4, 2, 3]

dp = [[-1] * 9  for _ in range(6)]


# for i in range(1, 6):
#     for j in range(1, 9):
#         if j == weight[i]:
#             dp[i][j] = max(dp[i - 1][j], price[i])
#         else:
#             dp[i][j] = dp[i - 1][j]
#         if dp[i][j - weight[i]]:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + price[i])


dp[1][0] = 0
dp[1][weight[1]] = price[1]
for i in range(2, 6):
    for j in range(9):
        if j - weight[i] >= 0 and dp[i - 1][j - weight[i]] != -1:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + price[i])
        else:
            dp[i][j] = dp[i - 1][j]
pprint(dp)


# weight = [3, 1, 4, 5, 2]
# price = [4, 1, 2, 6, 3]
weight = [2, 6, 2, 3, 4]
price =  [3, 5, 4, 2, 3]
n = 8
dp = [[-1] * 9 for _ in range(5)]

dp[0][0] = 0
dp[0][weight[0]] = price[0]

for i in range(1, 5):
    for j in range(n+1):
        if j - weight[i] >= 0 and dp[i-1][j-weight[i]] != -1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + price[i])
        else:
            dp[i][j] = dp[i-1][j]
for i in range(5):
    print(dp[i])
