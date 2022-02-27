n = int(input())
s = input()

m = 0
total = 0
for i in s:
    total += (ord(i) - 96) * 31 ** m
    m += 1
print(total % 1234567891)
