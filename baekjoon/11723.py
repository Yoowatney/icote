import sys

input = sys.stdin.readline
s = set()

def solution(c):
    global s
    if c[0] != "empty" and c[0] != "all":
        c[1] =  int(c[1])
    if c[0] == "add":
        s.add(c[1])
    elif c[0] == "remove":
        if s != set():
            s.remove(c[1])
    elif c[0] == "check":
        print(1) if c[1] in s else print(0)
        # if c[1] in s:
        #     print(1)
    elif c[0] == "toggle":
        s.remove(c[1]) if c[1] in s else s.add(c[1])
    elif c[0] == "all":
        s = {i for i in range(1, 21)}
    else:
        s = set()

for i in range(int(input())):
    solution(input().split())
