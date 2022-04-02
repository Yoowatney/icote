from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

ret = 0
comb = list(combinations(card, 3))
for l in comb:
    total = sum(l)
    if ret < total < m:
        ret = total
    elif total == m:
        print(m)
        exit(0)
print(ret)

# temp = 0
# for i in range(0, n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             val = card[i] + card[j] + card[k]
#             if temp < val <= m:
#                 temp = val
# print(temp)
