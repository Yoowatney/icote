from collections import deque

n, m = map(int, input().split())
l = deque(map(int, input().split()))
q = deque(range(1, n + 1))
total = 0

while l:
    k = 0
    r = 0 # r = 0일땐 -
    n = len(q)
    for i in range(n):
        if q[i] == l[0]:
            if n - i > i: # 앞으로 가는게 더 빠름
                k = i
                r = 0
            else: # 뒤로 가는게 더 빠름
                k = n - i
                r = 1
    if r == 1:
        q.rotate(k)
    else:
        q.rotate(-k)
    q.popleft()
    l.popleft()
    total += k
print(total)
