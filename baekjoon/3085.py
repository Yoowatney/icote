import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
def count():
    count = 1
    ret = 0
    for i in range(n): # 행
        for j in range(n):
            if j + 1 < n and arr[i][j] == arr[i][j + 1]:
                count += 1
            else:
                ret = max(count, ret)
                count = 1
        if ret == n:
            return n
    for i in range(n): # 열
        for j in range(n):
            if j + 1 < n and arr[j][i] == arr[j + 1][i]:
                count += 1
            else:
                ret = max(count, ret)
                count = 1
        if ret == n:
            return n
    return ret

def solution():
    ret = 0
    for i in range(n):
        for j in range(n):
            if 0 <= j + 1 < n and arr[i][j] != arr[i][j + 1]:
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                ret = max(ret, count())
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            if 0 <= j + 1 < n and arr[j][i] != arr[j + 1][i]:
                arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
                ret = max(ret, count())
                arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
    return ret
print(solution())
