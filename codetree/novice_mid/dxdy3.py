n, t = map(int, input().split())
r,c,d = input().split()
x = int(r)
y = int(c)
dys = [1, 0, -1, 0]
dxs = [0, -1, 0, 1]
dirs = { # mapper 라는 함수명으로 바꿔도 좋을듯
        "R" : 0,
        "U" : 1,
        "L" : 2,
        "D" : 3
        }
dir_num = dirs[d]

def in_range(x, y):
    return 1 <= x < n + 1 and 1 <= y < n + 1

while t:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        dir_num = (dir_num + 2) % 4
    t -= 1

print(x, y)
