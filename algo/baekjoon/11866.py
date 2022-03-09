from collections import deque

n, m = map(int, input().split())
q = deque(range(1, n + 1))
l = []
while q:
    for i in range(1, m):
        q.append(q.popleft())
    l.append(q.popleft())
print(f'<{str(l)[1:-1]}>')
