# n = int(input())
# arr = list(map(int, input().split()))
#
# val = [0] * n
# for i in range(n):
#     for j in range(i):
#         if arr[j] < arr[i]:
#             val[i] += arr[j]
#     val[i] += arr[i]
# print(arr)
# print(val)
# print(max(val))
# print(val)

# val = [0] * n
# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n
# # dp[0] = arr[0]
#
# for i in range(n):
#     temp = []
#     for j in range(i - 1, -1, -1):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[j] + arr[i], dp[i])
#     if dp[i] == 0:
#         dp[i] = arr[i]
# print(dp)
# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + arr[i], dp[i])
    if dp[i] == 0:
        dp[i] = arr[i]
print(max(dp))
