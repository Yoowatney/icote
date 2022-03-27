# from collections import deque
# from time import time
#
#
# a = deque([1])
# for i in range(1000):
#     a.append(5)
# start_time = time()

# print(a[999])
# end_time = time()
#
# print("== deque ==")
# print(end_time - start_time)
#
# a = [1]
# for i in range(10000):
#     a.append(5)
# start_time = time()
# print(a[999])
# end_time = time()
#
# print("== list ==")
# print(end_time - start_time)


import sys

input = sys.stdin.readline

print(input().split())

print("Hello")
