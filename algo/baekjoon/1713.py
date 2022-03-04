

# a = {2 : 4, 3 : 2, 1 : 4}
# print(sorted(a.values()))

# a.sort(key=lambda x:(x.items()))




# d = {i : 0 for i in range(1, 101)}
# size = int(input())  # 3
# int(input()) # 9
# arr = list(map(int, input().split()))
# for i in arr:
#     d[i] = d[i] + 1
# print(d)
# sorted(d.items(), key=lambda item:item[1])

# frame = [0 for _ in range(int(input()))]

from collections import deque

def swapByTable(table, a):
    for i in range(size):
        for j in range(i + 1, size):
            if (table[a[i]] > table[a[j]]):
                a[i], a[j] = a[j], a[i]

def back(table, a, i):
    temp = 0
    for k in range(size):
        if table[a[k]] == i:
            temp = k
    # for k in a:
    #     if table[k] == i:
    #         temp = k
    return temp

size = int(input())
int(input())

table = [0] * 101

a = []

a = deque()

li = list(map(int, input().split()))
for i in li:
    print(a)
    if len(a) < size and table[i] == 0:
        a.append(i)
    else: # len(a) == size
        if table[i] == 0:
            table[a.popleft()] = 0
            a.append(i)
        table[i] += 1
        back(table, a, i)
        swapByTable(table, a)
print(a)
print(table)

# table[2] = 1
# table[3] = 4
# table[4] = 1

# a = deque()
#
# a.append(2)
# a.append(3)
# a.append(4)
