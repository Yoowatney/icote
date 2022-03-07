import sys
from collections import Counter

input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]

# def round(arr):
#     num = sum(arr) / len(arr)
#     if (abs(num) - abs(int(num))) < 0.5:
#         return int(num)
#     else:
#         return int(num) + 1

def n_round(arr):
    num = sum(arr) / len(arr)
    if (abs(num) - abs(int(num))) < 0.5:
        return int(num)
    else:
        return int(num) - 1

def round(arr):
    s = sum(arr)
    if s >= 0:
        return int((s / len(arr)) + 0.5)
    else:
        return int((s/ len(arr)) - 0.5)


def median(arr):
    
    idx = len(arr) // 2
    if len(arr) % 2 == 1:
        return arr[idx]
    else:
        return arr[idx]

s_arr = sorted(arr)
l = Counter(arr).items()

print(round(arr))
# print(round(arr)) if sum(arr) >= 0 else print(n_round(arr))

print(s_arr[len(arr) // 2])
s_l = sorted(l, key=lambda x:(x[1]), reverse=True)
if len(s_l) >= 2 and s_l[0][1] == s_l[1][1]:
    temp = []
    for num, fre in s_l:
        if fre == s_l[0][1]:
            temp.append(num)
    temp.sort()
    print(temp[1])
else:
    print(s_l[0][0])
print(s_arr[len(arr) - 1] - s_arr[0])
