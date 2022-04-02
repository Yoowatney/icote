def greater_than_two(n):
    if n == 1:
        print(d[1])
        return 0
    elif n == 2:
        print(d[1] + d[2])
        return 0
    return 1

n = int(input())
d = [0]
for _ in range(n):
    d.append(int(input()))

f = [0] * (n + 1)
f[0] = 0

if greater_than_two(n):
    f[1] = d[1]
    f[2] = d[2] + d[1]
    for i in range(3, n + 1):
        f[i] = max(f[i - 2], f[i - 3] + d[i - 1]) + d[i]
    print(f[n])
