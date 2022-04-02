#!/usr/bin/env python3

# from pprint import pprint
# import sys
#
# n, m = map(int, input().split(' '))
#
# arr = []
# arr.append(list(input()))
# for _ in range(n - 1):
#     arr.append(list(sys.stdin.readline().rstrip()))
#
# form1 = list("BWBWBWBW")
# form2 = list("WBWBWBWB")
# count = 100
# for i in range(n - 7):
#     for j in range(m - 7):
#         index = 0
#         count1 = 0
#         count2 = 0
#         for ii in range(i, i + 8):
#             for jj in range(j, j + 8):
#                 if (ii % 2 == 0 and arr[ii][jj] != form1[jj - j]):
#                     count1 += 1
#                 elif (ii % 2 != 0 and arr[ii][jj] != form2[jj - j]):
#                     count1 += 1
#         for ii in range(i, i + 8):
#             for jj in range(j, j + 8):
#                 if (ii % 2 == 0 and arr[ii][jj] != form2[jj - j]):
#                     count2 += 1
#                 elif (ii % 2 != 0 and arr[ii][jj] != form1[jj - j]):
#                     count2 += 1
#         count = min(count1, count2, count)
# print(count)


w = "w", "b"

print(w)
