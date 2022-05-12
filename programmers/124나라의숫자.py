# from itertools import product
# def solution(n):
#     prefix = 0
#     suffix = 0
#     ret = []
#     for i in range(18):
#         prefix = (3**(i + 1) - 3) // 2
#         suffix = (3** (i + 2) - 3) // 2
#         if prefix <= n <= suffix:
#             ret = list(product(a, repeat=i+1))
#             break
#     return "".join(str(i) for i in ret[n - prefix - 1])

def solution(n):
    arr = [1,2,4]
    answer = []
    while n:
        answer.append(arr[(n - 1) % 3])
        n = (n - 1) // 3
    answer.reverse()
    return "".join(str(i) for i in answer)

solution(10)

# for i in list(product([1,2,4], repeat=14)):

# print(*product(a, repeat=1))
# print(*product(a, repeat=2))
# solution(7)

# for i in ret:
#     print(i)

# count = 0
# for i in ret:
#     print(i)
#     count += 1
