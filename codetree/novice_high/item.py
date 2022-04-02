n = 8
coin = [1, 4, 5]

dp = [0] * 9

for i in range(1, n + 1):
    _min = 1000
    for j in range(len(coin)):
        if coin[j] <= i:
            _min = min(dp[i - coin[j]] + 1, _min)
    dp[i] = _min
print(dp)

