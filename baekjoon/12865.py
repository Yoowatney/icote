from pprint import pprint
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

w = [0] # 무게
p = [0] # 가치

for _ in range(n):
    a, b = map(int ,input().split())
    if a > k:
        continue
    w.append(a)
    p.append(b)

dp = [[0] * (k + 1) for _ in range(n + 1)]

ret = 0
if len(w) >= 2:
    dp[1][w[1]] = ret = p[1]
for i in range(2, len(w)): # 2 ~ 4
    for j in range(1, k + 1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + p[i])
        else:
            dp[i][j] = dp[i - 1][j]
        ret = max(ret, dp[i][j])
print(ret)

# pprint(dp)
# print(dp[n][k], n, k)
# temp = 0
# for i in range(n + 1):
#     temp = max(temp, max(dp[i]))
# print(temp)


import sys
input=sys.stdin.readline

n,k=map(int,input().split())
bag=[0]*(k+1)
# l=[list(map(int,input().split())) for _ in range(n)]

for _ in range(n):
	w,v=map(int,input().split())
	for j in range(k,w-1,-1):
		bag[j]=max(bag[j],bag[j-w]+v)
print(bag[-1])
