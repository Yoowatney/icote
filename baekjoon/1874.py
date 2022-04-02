from collections import deque
import sys
input = sys.stdin.readline
# n = list(range(1, int(input()) + 1)) # n = [1,2,3,4,5]
n = deque(range(1, int(input()) + 1))

s = []
solution = []
prev = 0
for _ in range(len(n)): # 100000
    m = int(input())
    if prev < m:
        for i in range(m - prev):
            s.append(n.popleft())
            solution.append("+")
        s.pop()
        solution.append("-")
        prev = m
    else: # prev > m
        if s[-1] == m:
            s.pop()
            solution.append("-")
        else:
            print("NO")
            exit(0)
print(*solution, sep="\n")

