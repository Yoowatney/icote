import sys
from collections import deque

input = sys.stdin.readline
q = deque()
def command(c, n):
    if c[0] == 'f':
        print(q[0]) if len(q) else print(-1)
    if c[0] == 'b':
        print(q[-1]) if len(q) else print(-1)
    if c[0] == 'e':
        print(0) if len(q) else print(1)
    if c[0] == 's':
        print(len(q))
    if c[1] == 'u':
        q.append(n)
    if c[1] == 'o':
        print(q.popleft()) if len(q) else print(-1)

for _ in range(int(input())):
    l = input().split()
    c = l[0]
    n = -1
    if len(l) > 1:
        n  = l[1]
    command(c, n)
