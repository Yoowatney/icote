#!/usr/bin/env python3

def process():
    a = []
    for i in list(input()):
        if i == '(': a.append('(')
        else :
            if a != []: a.pop()
            else :
                a = [1]
                break
    if a == []: print("YES")
    else : print("NO")

for _ in range(int(input())):
    process()







for _ in range(int(input())):
    a = []
    for s in input():
        if s == "(":
            a.append("(")
        else:
            if a:
                a.pop()
            else:
                a = [1]
                break
    if a:
        print("NO")
    else:
        print("Yes")
