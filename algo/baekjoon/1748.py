#!/usr/bin/env python3

# arr = []
# for i in range(1, int(input()) + 1):
#     arr.append(str(i))
#     # _str = "".join(str(i))
#     print(arr)
# _str = "".join(arr)
# print(_str, len(_str))
#
def solution(n):
    return sum(map(lambda x : len(str(x)), range(1, n + 1)))
print(solution(int(input())))
# _str = input()
# n = len(_str)
# val = 0
# for i in range(1, n):
#     val += i * 9 * 10**(i - 1)
# val += n * (int(_str) - 10**(n - 1) + 1)
# print(val)
