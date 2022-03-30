# from itertools import product
# 중복순열을 구하는 문제와 같다
k, n = map(int, input().split())

__import__('pprint').pprint([1,2,3])
arr = [0] * n
def choose(num):
    if num == n + 1:
        print(*arr)
        return
    for i in range(1, k + 1):
        arr[num - 1] = i
        choose(num + 1)
choose(1)
