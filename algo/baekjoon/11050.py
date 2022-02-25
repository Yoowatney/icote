n,k = map(int, input().split())
div = 1
total = 1
for i in range(1, k + 1):
    div *= i
    total *= n
    n -= 1
print(total // div)
