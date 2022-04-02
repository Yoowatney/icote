n,k = map(int, input().split())

def factorial(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret

print(factorial(n) // (factorial(n - k) * factorial(k)))
print(int(factorial(n) / (factorial(n - k) * factorial(k))))
