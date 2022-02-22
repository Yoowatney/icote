
x = int(input())

d = [0] * 30001
# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

def dp(x):
    if x == 1:
        return 0
    if d[x] != 0:
        return d[x]
    d[x] = dp(x - 1) + 1
    if x % 5 == 0:
        d[x] = min(d[x], dp(x // 5) + 1)
    if x % 4 == 0:
        d[x] = min(d[x], dp(x // 3) + 1)
    if x % 2 == 0:
        d[x] = min(d[x], dp(x // 2) + 1)
    return d[x]





def my_dp(x):
    if x == 1:
        return 0
    if d[x] != 0:
        return d[x]
    d[x] = dp(x - 1) + 1
    if x % 5 == 0:
        d[x] = min(d[x], dp(x // 5) + 1)
    if x % 3 == 0:
        d[x] = min(d[x], dp(x // 3) + 1)
    if x % 2 == 0:
        d[x] = min(d[x], dp(x // 2) + 1)
    return d[x]

for x in range(2, 30000):
    d[x] = d[x - 1] + 1
    if x % 5 == 0:
        d[x] = min(d[x // 5] + 1, d[x])
    if x % 3 == 0:
        d[x] = min(d[x // 3] + 1, d[x])
    if x % 2 == 0:
        d[x] = min(d[x // 2] + 1, d[x])

print(d[5])


# print(my_dp(5))
# print(my_dp(6))
# print(my_dp(7))
