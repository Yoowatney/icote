# a = [1,5,4,3,5,7,8,4,2,3]
#
# s_a = sorted(a)
# print(s_a)

from collections import deque


def lower_bound(arr, val):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        print(lo, mid, hi)
        if arr[mid] < val:
            lo = mid + 1
        # elif arr[mid] == val:
        #     return mid
        else:
            hi = mid
    return lo

# print(lower_bound([1,2,3,4,5], 3))




def lower_bound2(arr, val):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid
    return lo

# print(lower_bound2([1,2,3,3,3,3,3,4,5], 3))


def upper_bound(arr, val):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid
    return lo + 1
        
# print(upper_bound([1,2,3,3,3,3,3,4,5], 3))

a = deque(range(1,3))
print(a)
