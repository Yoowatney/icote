d = [0] * 12

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    if d[n] != 0:
        return d[n]
    d[n] = dp(n - 3) + 4 + dp(n - 2) + 2+ dp(n - 1) + 1
    return d[n]



# print(dp(4))

d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 12):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]
for _ in range(int(input())):
    print(d[int(input())])

