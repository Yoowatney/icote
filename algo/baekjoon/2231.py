n = int(input())

for num in range(1, 1000001):
    total = num
    for s in str(num):
        total += int(s)
    if n == total:
        print(num)
        break
    if num >= n:
        print(0)
        break
