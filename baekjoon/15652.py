from itertools import combinations_with_replacement

n,m = map(int, input().split())

arr = []
def solution(num):
    if num > m:
        print(*arr)
        return
    for i in range(1, n + 1):
        if arr == [] or arr[-1] <= i:
            arr.append(i)
            solution(num + 1)
            arr.pop()
# solution(1)


# print(*combinations_with_replacement([i for i in range(1, n + 1)], m), sep="\n")

temp = combinations_with_replacement([i for i in range(1, n + 1)], m)
for ret in temp:
    print(*ret)
