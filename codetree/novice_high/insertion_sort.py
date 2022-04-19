# selection sort

import random


arr = []
for _ in range(10):
    arr.append(random.randint(1, 100))
print(arr)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j += -1
    arr[j + 1] = key
print(arr)
