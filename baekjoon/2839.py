n = int(input())

for i in range(n // 5, -1, -1):
    if (n - 5 * i) % 3 == 0:
        f = i
        t = (n - 5 * i) // 3
        print(f + t)
        exit(0)
print(-1)
