#!/usr/bin/env python3

def process():
    a = []
    for i in list(input()):
        if len(a) == 0 or a[-1] != i: a.append(i)
        else: a.pop() 
            # else: a.append(i)
        # elif len(a) == 1:
        #     if (a[0] == i): a.pop()
        #     else: a.append(i)
        # else:
        #     if (a[len(a) - 1] == i): a.pop()
        #     else : a.append(i)
        #         # a.pop() != i:return(0)
    if (len(a) != 0):
        return (0)
    return (1)

count = 0
for _ in range(int(input())):
    count += process()
print(count)

