
n = int(input())
d = [n]
_max = 0
temp = []
for i in range(1, n + 1):
    d = [n]
    d.append(i)
    while True:
        num = d[len(d) - 2] - d[len(d) - 1]
        if num >= 0:
            d.append(num)
        else:
            if len(d) > _max:
                _max = len(d)
                temp = d
                # temp = copy.deepcopy(d)
            break
print(len(temp))
print(*temp)
