
n, m = map(int, input().split())

# from itertools import product
# arr = [i for i in range(1, n + 1)]
#
# for ret in product(arr, repeat=m):
#     print(*ret)

arr = []

def pro(num):
    if num > m:
        print(*arr)
        return
    for i in range(1, n + 1):
        arr.append(i)
        pro(num + 1)
        arr.pop()
pro(1)


