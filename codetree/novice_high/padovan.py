a = [1, 1, 1, 2, 2] + [-1 for _ in range(100)]
for i in range(5, 100):
    a[i] = a[i - 1] + a[i - 5]

def padovan(n):
    return a[n]
for _ in range(int(input())):
    print(padovan(int(input()) - 1))
print(a)
