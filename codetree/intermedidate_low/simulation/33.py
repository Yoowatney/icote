n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def region_sum(r, c):
    count = 0
    for row in range(r, r + 3):
        for col in range(c, c + 3):
            if arr[row][col] == 1:
                count += 1
    return count
ret = 0
for row in range(0, n - 2):
    for col in range(0, n - 2):
        ret = max(ret, region_sum(row, col))
print(ret)
# for i in range(n):
#     print(*arr[i])
