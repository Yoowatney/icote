from collections import deque

n,k = map(int, input().split())
q = deque(list(range(1, n + 1)))
while q:
    q.rotate(-k + 1)
    print(q.popleft(), end=" ")
