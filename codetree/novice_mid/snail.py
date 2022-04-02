n, m = map(int, input().split())

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

arr = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dir_num = 1
x = y = 0

arr[0][0] = 1
count = 2
while True:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = count
        count += 1
        x, y= nx, ny
    else:
        dir_num = (dir_num + 1) % 4
    if count == n * m + 1:
        break

for i in range(n):
    print(*arr[i])

