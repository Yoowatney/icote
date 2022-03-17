int(input())

arr = list(map(int, input().split()))
n = len(arr)

# for i in range(n):
#     for j in range(i, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

_sorted = False
while not _sorted:
    _sorted = True
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            _sorted = False
print(arr)
