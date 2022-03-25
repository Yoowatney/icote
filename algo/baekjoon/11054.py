import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reverse_arr = list(reversed(arr))

dp = [0] * n
reverse_dp = [0] * n
for i in range(n):
    temp = []
    for j in range(i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if temp:
        dp[i] = max(temp) + 1
    else: dp[i] = 1

for i in range(n):
    temp = []
    for j in range(i):
        if reverse_arr[j] < reverse_arr[i]:
            temp.append(reverse_dp[j])
    if temp:
        reverse_dp[i] = max(temp) + 1
    else: reverse_dp[i] = 1
reverse_dp = list(reversed(reverse_dp))

ret = 0
for i in range(n):
    ret = max(ret, reverse_dp[i] + dp[i])
print(ret - 1)

# print("== arr ==")
# print(arr)
# print()
# print("== dp ==")
# print(dp)
# print()
# print("== reverse_dp ==")
# print(reverse_dp)
# print()

# for i in range(1, n):
#     pivot = arr[i]
#     lds_dp = lis_dp[:]
#     for j in range(i + 1, n):
#         if pivot > arr[j]:
#             pivot = arr[j]
#             lds_dp[j] = lds_dp[i] + 1
#     print(lds_dp, i)
# print(lis_dp)
