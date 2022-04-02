n = int(input())
nn = 0

arr = [list(map(int, input().split())) for _ in range(n)]

region = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            region.append([i,j])
            nn += 1

dxss = [[-1, 1, 0, 0], [1, -1, 2, -2], [1, 1, -1, -1]]
dyss = [[0, 0, -1, 1], [0, 0, 0, 0], [1, -1, 1, -1]]

ret = 0

def count_region():
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] < 0 or arr[i][j] == 100:
                count += 1
    return count

def is_range(x, y):
    return 0 <= x < n and 0 <= y <n

def bomb(i, j, c):
    if c == "b":
        arr[i][j] = -2
        for dxs, dys in zip(dxss, dyss):
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_range(nx, ny) and arr[nx][ny] == 0:
                    arr[nx][ny] = -1
    else:
        arr[i][j] = 1
        for dxs, dys in zip(dxss, dyss):
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_range(nx, ny) and arr[nx][ny] == -1:
                    arr[nx][ny] = 0

def choose(idx):
    global ret
    if idx == nn:
        ret = max(count_region(), ret)
        # for i in range(n):
        #     print(arr[i])
        # print()
        return
    i = region[idx][0]
    j = region[idx][1]
    for dxs, dys in zip(dxss, dyss):
        arr[i][j] = 100
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if is_range(nx, ny) and arr[nx][ny] <= 0:
                arr[nx][ny] -= 1
        choose(idx + 1)
        arr[i][j] = 1
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if is_range(nx, ny) and arr[nx][ny] < 0:
                arr[nx][ny] += 1
        # for k in range(n):
        #     print(arr[k])
        # print("위에는 끝나고 난후")
choose(0)
print(ret)
