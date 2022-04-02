#!/usr/bin/env python3
int(input())
count = 0
for num in list(map(int, input().split())):
    if (num == 2):
        count += 1
    for i in range(2, num):
        if (num % i == 0):
            break 
        if (i == num - 1):
            count += 1
print(count)
