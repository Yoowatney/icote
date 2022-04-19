from itertools import combinations

h, w, k = map(int, input().split())
board = [list(map(int, input().split())) for __ in range(h)]

res = -9e999

for t in combinations(((r, c) for r in range(h) for c in range(w)), k):
    f = False
    for [(r1, c1), (r2, c2)] in combinations(t, 2):
        if abs(r1 - r2) + abs(c1 - c2) == 1:
            break
    else:
        f = True
    if not f:
        continue
    res = max(res, sum(board[r][c] for r, c in t))

print(res)

