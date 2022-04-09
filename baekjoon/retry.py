import sys
input = sys.stdin.readline

n = int(input())
c = [list(input().rstrip()) for _ in range(n)]
r = 1

def e():
    global r
    for i in range(n):
        t = 1
        for j in range(n):
            if j+ 1 < n and c[i][j] == c[i][j + 1]:
                t += 1
            else:
                r = max(r, t)
                t = 1
        r = max(r, t)
    for i in range(n):
        t = 1
        for j in range(n):
            if j + 1 < n and c[j][i] == c[j + 1][i]:
                t += 1
            else:
                r = max(r, t)
                t = 1
        r = max(r, t)
        
for i in range(n):
    for j in range(1, n):
        c[i][j], c[i][j-1] = c[i][j-1], c[i][j]
        e()
        c[i][j], c[i][j-1] = c[i][j-1], c[i][j]
        c[j][i], c[j-1][i] = c[j-1][i], c[j][i]
        e()
        c[j][i], c[j-1][i] = c[j-1][i], c[j][i]
print(r)
