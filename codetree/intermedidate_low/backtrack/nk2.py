k, n = tuple(map(int, input().split()))

arr = [0] * n

def overlap(): # O(K*N^2)
    for i in range(1, k + 1): # O(k)
        if str(i)*3 in ''.join(str(n) for n in arr): # O(N * N)
            return True
    return False

def choose(num):
    if num == n + 1: # O(K^N)
        if not overlap():
            print(*arr)
        return
    for i in range(1, k + 1): # O(N^K)
        arr[num - 1] = i
        choose(num + 1)
    pass
# choose(1)

# def backtracking_choose(num): # backtracking
#     if num == n + 1: # O(K^N)
#         print(*arr)
#         return
#     for i in range(1, k + 1):
#         if num >= 3 and arr[-1] == i and arr[-2] == i:
#             continue
#         arr[num - 1] = i
#         choose(num + 1)
# backtracking_choose(1)
choose(1)
