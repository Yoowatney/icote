e, s, m = map(int, input().split())

num = 1
while True:
    a = num % 15
    if a == 0:
        a = 15
    b = num % 28
    if b == 0:
        b = 28
    c = num % 19
    if c == 0:
        c = 19
    if a == e and b == s and c == m:
        print(num)
        break
    num += 1
