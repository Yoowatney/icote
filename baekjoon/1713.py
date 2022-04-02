# n, m = int(input()), int(input())
# frames = dict()
#
#
# def test(x):
#     print("=========")
#     print(x)
#     return frames[x]
#
# cnt = 0
# for reco in map(int, input().split()):
#     if len(frames) >= n and not reco in frames:
#         print(frames)
#         del frames[min(frames, key=test)]
#     try: frames[reco][0] += 1
#     except:
#         frames[reco] = [1, cnt]
#         cnt += 1
# print(*sorted(frames.keys()))

# def test(x):
#     print("====")
#     print(x)
#     return (x)
# b = [1,2,3,4]
#

# from typing import OrderedDict
#
#
# a = {4: [3,0], 1 : [2, 2], 2 : [2, 0], 3 : [2, 0]}
# print(sorted(a, key=lambda x:(a[x])))

# order = OrderedDict()

# order[3] = 1
# order[4] = 2
# order[5] = 3
# order[6] = 4
# print(order)


# print(min(a, key=test))


# n, m = int(input()), int(input())
# frames = dict()
#
# for reco in map(int, input().split()):
#     if len(frames) >= n and not reco in frames:
#         del frames[min(frames, key=lambda x:frames[x])]
#     try: frames[reco][0] += 1
#     except:
#         frames[reco] = [1]
#
# print(*sorted(frames.keys()))
#
# print(min(a, key=lambda x: a[x]))


# print(d)
# print(d.keys())


# frame = [0 for _ in range(int(input()))]

# from collections import deque
#
# size = int(input())
# int(input())
#
#
# picture = deque()
# count = 0
# for num in map(int, input().split()):
#     temp = []
#     if picture:
#         temp = list(zip(*picture))[0]
#     if num in temp:
#         for i in range(len(picture)):
#             if picture[i][0] == num:
#                 picture[i][1] += 1
#     else: # not in picture
#         count += 1
#         if len(picture) >= size:
#             picture.popleft()
#         picture.append([num, 1, count])
#     picture = deque(sorted(picture, key=lambda x:(x[1], x[2])))
# picture = sorted(picture)
# for a,b,c in picture:
#     print(a, end=" ")
#
# n, m = int(input()), int(input())
# frames = dict()
#
# cnt = 0
# for reco in map(int, input().split()):
#     if len(frames) >= n and not reco in frames:
#         del frames[min(frames, key=lambda x:frames[x])]
#     try: frames[reco][0] += 1
#     except:
#         frames[reco] = [1, cnt]
#         cnt += 1
#
# print(*sorted(frames.keys()))

# table = []
# # picture = []
# picture = deque()
#
# for num in map(int, input().split()):
#     if num in picture: # picture안에 있다
#         for i in range(len(picture)):
#             if picture[i] == num:
#                 table[i] += 1
#     else: # picture안에 없다
#         if len(picture) >= size: # 없는데 full
#             for i in range(len(table)): # table 가장 작고 인덱스 처음값 삭제
#                 if min(table) == table[i]:
#                     del table[i], picture[i]
#                     break
#         picture.append(num)
#         table.append(1)
# print(*sorted(picture))

# for num in map(int, input().split()):
#     if num in picture: # picture안에 있다
#         for i in range(len(picture)):
#             if picture[i] == num:
#                 table[i] += 1
#     else: # picture안에 없다
#         if len(picture) >= size: # 없는데 full
#             for i in range(len(table)): # table 가장 작고 인덱스 처음값 삭제
#                 if min(table) == table[i]:
#                     del table[i], picture[i]
#                     break
#         picture.append(num)
#         table.append(1)
# print(*sorted(picture))




# table[2] = 1
# table[3] = 4
# table[4] = 1

# a = deque()
#
# a.append(2)
# a.append(3)
# a.append(4)
