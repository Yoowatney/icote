arr = [0] * 11

arr[-1] = 1
arr[-2] = -1
for i in range(-3, -11, -1):
    arr[i] = arr[i + 2] - arr[i + 1]
print(arr)
