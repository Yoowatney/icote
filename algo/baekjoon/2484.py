#!/usr/bin/env python3

def money(idx, max_val):
    ret = 0
    if (max_val == 4):
        ret = 50000 + (idx + 1) * 5000
    elif (max_val == 3):
        ret = 10000 + (idx + 1) * 1000
    elif (max_val == 2):
        ret = 1000 + (idx + 1) * 100
    elif (max_val == 1):
        ret = (idx + 1) * 100
    return ret

count_lists = []
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    _list = []
    for i in range(1, 7):
        _list.append(arr.count(i))
    count_lists.append(_list)

ret = 0
for count_list in count_lists:
    val = max(count_list)
    temp = 0
    if (count_list.count(2) == 2):
        for i in range(6): # count_list 속에 2가 있다면으로 바꿔보자
            if count_list[i] == 2:
                temp += i + 1
        ret = max(ret, 2000 + temp * 500)
    elif (val == 1):
        count_list.reverse()
        ret = max(ret, money(5 - count_list.index(1), val))
    else:
        ret = max(ret, money(count_list.index(val), val))
print(ret)
