arr = [60, 65, 50, 70, 63, 55, 45, 51, 45, 48, 54, 70, 61]

n = len(arr)
dp = [1] * n

for i in range(n):
    temp = []
    for j in range(i):
        if arr[j] > arr[i]:
            temp.append(dp[j])
    if not temp:
        continue
    dp[i] = max(temp) + 1
print(arr)
print(dp)
