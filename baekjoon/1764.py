import sys
input = sys.stdin.readline

n,m = map(int, input().split())
deub = {input().rstrip() for _ in range(n)}
bo = {input().rstrip() for _ in range(m)}

ret = deub.intersection(bo)
print(len(ret))
print(*sorted(ret), sep="\n")
