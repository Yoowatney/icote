n = int(input())

for num in range(1, 10000000):
    if '666' in str(num):
        n -= 1
    if not n:
        print(num)
        exit(0)
