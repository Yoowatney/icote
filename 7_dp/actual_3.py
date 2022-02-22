# n = int(input())
#
# d = list(map(int, input().split()))
# d.insert(0, 0)
#
# f = [0] * (n + 1)
#
# for i in range(1, n + 1):
#     if i == 1:
#         f[1] = d[1]
#     elif i == 2:
#         f[2] = d[2]
#     else:
#         f[i] = max(f[1:i-1]) + d[i]
# print(f)


n = int(input())
arr = list(map(int, input().split()))
dp = [0]*100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])
print(dp[n-1])
print(dp)
