n,k = map(int, input().split())
li = list(map(int, input().split()))

print(li)

def bis_left(arr, val):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = (lo + hi)//2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

def lower_bound(arr, val):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(bis_left([1,2,3,3,3,3,4,5], 3))
print(lower_bound([1,2,3,3,3,3,4,5], 3))
