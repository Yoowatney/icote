n, m = map(int, input().split())
card = list(map(int, input().split()))

temp = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            val = card[i] + card[j] + card[k]
            if temp < val <= m:
                temp = val
print(temp)
