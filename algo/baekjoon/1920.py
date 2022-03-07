from bisect import bisect_left, bisect_right

import sys
input=sys.stdin.readline
int(input())
# a = sorted(list(map(int, input().split())))

a = set(map(int, input().split()))

int(input())
b = list(map(int, input().split()))

# for num in b:
#     print(1 if (bisect_right(a, num) - bisect_left(a, num)) else 0)


for i in b:
    # if i in a:
    #     print(1)
    # else:
    #     print(0)
    print(1 if i in a else 0)

# nums = [0,1,2,4,5,6,7,8,9]
# print(bisect_left(nums, 3))
# print(bisect_right(nums, 3))


