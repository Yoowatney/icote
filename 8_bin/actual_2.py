n = int(input())
component = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))


def binary_search(component, x):
    start = 0
    end = len(component) - 1
    while start <= end:
        mid = (start + end) // 2
        if component[mid] == x:
            return "Yes"
        elif x < component[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return "No"

for i in check: # O(M)
    print(binary_search(component, i)) # * O(logN)

