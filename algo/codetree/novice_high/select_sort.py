int(input())

arr = list(map(int, input().split()))
n = len(arr)

for i in range(n - 1):
    minimum = i
    for j in range(i + 1, n):
        if arr[minimum] > arr[j]:
            minimum = j
    arr[minimum], arr[i] = arr[i], arr[minimum]
print(arr)
