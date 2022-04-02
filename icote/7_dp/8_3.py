# bottom-up
d = [0] * 100
d[1] = 1
d[2] = 1


for i in range(1, 98):
    d[i + 2] = d[i + 1] + d[i]
print(d)
