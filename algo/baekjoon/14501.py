days = []
pays = []
l = int(input())
for _ in range(l):
    n, m = map(int, input().split())
    days.append(n)
    pays.append(m)

pays.append(0)
days.append(0)

# day, pay 10개

dp = [0] * (l + 1) # dp 11개
for i in range(1, l + 1): # 1~9까지 루프를 돌음 => 10까지 돌음
    for j in range(0, i + 1):
        if days[j] + j <= i:
            if j == 0:
                dp[i] = dp[0] + pays[j]
                # print(dp, i , j)
                continue
            temp = max(dp[:j+1])
            dp[i] = max(temp + pays[j], dp[i])
            # print(dp, i, j)
print(max(dp))
