from itertools import combinations
n, m = map(int, input().split())

# arr = [i for i in range(1, n + 1)]
# for comb in combinations(arr, m):
#     print(*comb)

arr = [0] * m # m개의 배열
arr = []
def choose(num): # 전에 있던 arr값보다 더 커져야함
    if num > m:
        print(*arr)
        return
    for i in range(1, n + 1):
        if arr == [] or arr[-1] < i: #arr[num - 2] < i:
            arr.append(i)
            choose(num + 1)
            arr.pop()
choose(1)

# choose()


# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
