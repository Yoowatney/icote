h, m = map(int, input().split())
a = int(input())

total = h * 60 + m + a

print(total // 60 % 24, total % 60)
