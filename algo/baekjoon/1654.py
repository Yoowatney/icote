k, n = map(int, input().split())

l = [int(input()) for _ in range(k)]
l.sort()

# _max = 0
# try:
#     for num in range(2, 1000000):
#         temp = 0
#         for i in l:
#             temp += i // num
#         if temp < n:
#             raise Exception("!")
#         elif temp == n:
#             _max = num
# except:
#     print(_max)

_max = 0
a = 0
try:
    for num in range(1, l[0] + 1):
        temp = 0
        for i in l:
            a += 1
            temp += i // num
        if temp >= n:
            _max = num
        elif temp < n:
            raise Exception("!")
except:
    print(_max)
    print(a)
