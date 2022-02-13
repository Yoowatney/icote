#!/usr/bin/env python3

arr = []
for num in range(int(input()), int(input()) + 1):
    for i in range(1, num):
        if (num == 2):
            arr.append(num)
        if (i == 1):
            continue
        if (num % i == 0):
            break
        elif (i == num - 1):
            arr.append(num)
print(f'{sum(arr)}\n{arr[0]}' if arr else -1)

# g = lambda arr:[sum(arr), arr[0]]
# print(-1 if not arr else *g(arr), sep="\n")
# print(arr)
# print(*[sum(arr), arr[0]] if arr else -1, sep="\n")
