from collections import deque
import sys
input = sys.stdin.readline

q = deque()
def command(c, n):
    if c[0] == "s":
        print(len(q))
    elif c[0] == "f":
        print(q[0]) if len(q) else print(-1)
    elif c[0] == "b":
        print(q[-1]) if len(q) else print(-1)
    elif c[0] == "e":
        print(0) if len(q) else print(1)
    elif c[4] == "f":
        print(q.popleft()) if len(q) else print(-1)
    elif c[4] == "b":
        print(q.pop()) if len(q) else print(-1)
    elif c[5] == "f":
        q.appendleft(n)
    elif c[5] == "b":
        q.append(n)

for _ in range(int(input())):
    l = input().split()
    c = l[0]
    n = -1
    if len(l) > 1:
        n = int(l[1])
    command(c, n)
