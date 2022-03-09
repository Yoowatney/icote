import sys
input = sys.stdin.readline
l = []
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        l.append(num)
    else:
        l.pop()
print(sum(l))
