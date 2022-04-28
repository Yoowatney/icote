total = 100
n = int(input())
dp = [[0] * 10 for _ in range(total)]


for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, total):
    for j in range(10):
        if j == 0 and dp[i - 1][j]:
            dp[i][j + 1] += dp[i - 1][j]
            continue
        elif j == 9 and dp[i - 1][j]:
            dp[i][j - 1] += dp[i - 1][j]
            continue
        elif dp[i - 1][j]:
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j + 1] += dp[i - 1][j]
print(sum(dp[n - 1]) % 1000000000)
# pprint(dp)

# for n in range(10, 100):
#     num = str(n)
#     if abs(ord(num[0]) - ord(num[1])) == 1:
#         print(num)
# print("10~99")

# count = 0
# for n in range(100, 1001):
#     num = str(n)
#     if abs(ord(num[0]) - ord(num[1])) == 1 and abs(ord(num[1]) - ord(num[2])) == 1:
#         count += 1
# print("100~999")
# print(count)
#
# count = 0
#
# for n in range(1000, 10001):
#     num = str(n)
#     if abs(ord(num[0]) - ord(num[1])) == 1 and abs(ord(num[1]) - ord(num[2])) == 1 and abs(ord(num[2]) - ord(num[3])) == 1:
#         count += 1
# print("1000~9999")
# print(count)

#
# count = 0
# for n in range(10000, 100001):
#     num = str(n)
#     if abs(ord(num[0]) - ord(num[1])) == 1 and abs(ord(num[1]) - ord(num[2])) == 1 and abs(ord(num[2]) - ord(num[3])) == 1 and abs(ord(num[2]) - ord(num[3])) == 1:
#         count += 1
# print("10000~99999")
# print(count)
#
# count = 0
