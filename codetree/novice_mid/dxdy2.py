n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

ret = 0
for x in range(n):
    for y in range(n):
        # === 이부분은 함수로 만들어 빼는것도 좋을듯
        count = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                count += 1
        if count >= 3:
            print(x, y)
            ret += 1
print(ret)
