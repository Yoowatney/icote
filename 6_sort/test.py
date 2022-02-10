#!/usr/bin/env python3

fruits = {"banana": 0, "apple" : 1, "mango" : -1, "grape" : 5}

# print(fruits.keys())
# print(fruits.values())
# print(fruits.items())
print(fruits)
sorted1 = sorted(fruits.items(), key=lambda x:x[1])
print(sorted1)
