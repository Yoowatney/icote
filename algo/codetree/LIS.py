a = [20, 80, 10, 50, 55, 20, 60, 70, 5, 90]

n = len(a)
dp = [1] * len(a)

for i in range(n):
    temp = []
    for j in range(i):
        if a[j] < a[i]:
            # dp[i] = max(dp[i], dp[j] + 1)
            temp.append(dp[j])
    if temp == []:
        continue
    dp[i] = max(temp) + 1
print(dp)
