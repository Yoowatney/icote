from collections import deque

n = int(input())

# q = deque([i for i in range(1, n + 1)])
q = deque(range(1, n + 1))


num = 1
while len(q) > 1:
    q.popleft()
    num = q.popleft()
    q.append(num)
print(num)
