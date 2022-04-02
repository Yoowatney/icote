# import sys
# input=sys.stdin.readline
# print(*sorted(list({input().rstrip() for _ in range(int(input()))}), key=lambda x:(len(x), x)), sep='\n')


def compare(x1, x2):
    if len(x1) != len(x2):
        return len(x1) > len(x2)
    else:
        return x1 > x2


def qsort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = [x for x in arr if compare(pivot, x)]
    right = [x for x in arr if compare(x, pivot)]
    return qsort(left) + [pivot] + qsort(right)
 
word = [input() for _ in range(int(input()))]

print(qsort(word))
