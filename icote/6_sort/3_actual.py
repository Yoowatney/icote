#!/usr/bin/env python3

n = int(input())

dic = dict()
for _ in range(n):
    enter = input().split(" ")
    name = enter[0]
    score = int(enter[1])
    dic[name] = score
    # name = input()
    # score = int(input())
    # print(name, score)
# dic[1] = "Hello"
print(dic)
def setting(data):
    return data[1]
result = sorted(dic.items(), key=setting)
print(result)
for element in result:
    print(element[0], end=' ')
# for key in result.values():
#         print(key)
