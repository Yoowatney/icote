n = int(input())
# arr = [[0] * n for _ in range(n)]

arr = [0] * n


count = 0
# def put(num):
#     global count
#     if num >= n:
#         count += 1
#         for i in arr:
#             print(i)
#         print()
#         return
#     for i in range(num, n):
#         for j in range(n):
#             if 1 in arr[i]: # row
#                 continue
#             if 1 in [arr[k][j] for k in range(0, n)]: # column
#                 continue
#             if i <= j and (1 in [arr[k][j - i + k] for k in range(0, n) if 0 <= j - i + k < n] or 1 in [arr[k][j + i - k] for k in range(0, n) if 0 <= j + i - k < n]): # 하단 대각
#                 continue
#             if i > j and (1 in [arr[i - j + k][k] for k in range(0, n) if 0 <= i - j + k < n] or 1 in [arr[k][j + i - k] for k in range(0, n) if 0 <= j + i - k < n]):
#                 continue
#             arr[i][j] = 1
#             put(num + 1)
#             arr[i][j] = 0
# put(0)

def is_promising(num):
    for i in range(num):
        if arr[num] == arr[i] or abs(arr[num] - arr[i]) == abs(num - i):
            return False
    return True

def nqueen(num):
    global count
    if num >= n :
        count += 1
        return
    for i in range(n):
        arr[num] = i
        if is_promising(num):
            nqueen(num + 1)
nqueen(0)
print(count)
