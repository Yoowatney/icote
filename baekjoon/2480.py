l = sorted(list(map(int, input().split())))
s = set(l)
num = 0
if len(s) == 3: num = l[2] * 100
elif len(s) == 2: num = l[1] * 100 + 1000
elif len(s) == 1: num = l[0] * 1000 + 10000
print(num)
