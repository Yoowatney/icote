n = int(input())

f = [0] * (n + 3)
f[1] = 0
f[2] = 1
for i in range(1, n + 1):
    f[i + 2] = f[i + 1] + f[i]
print(f[n + 1])
