

# a = {2 : 4, 3 : 2, 1 : 4}
# print(sorted(a.values()))

# a.sort(key=lambda x:(x.items()))

# d = {i : 0 for i in range(1, 101)}
# size = int(input())  # 3
# int(input()) # 9
# arr = list(map(int, input().split()))
# for i in arr:
#     d[i] = d[i] + 1
# print(d)
# sorted(d.items(), key=lambda item:item[1])

# frame = [0 for _ in range(int(input()))]

from collections import deque

size = int(input())
int(input())


picture = deque()
count = 0
for num in map(int, input().split()):
    temp = []
    if picture:
        temp = list(zip(*picture))[0]
    if num in temp:
        for i in range(len(picture)):
            if picture[i][0] == num:
                picture[i][1] += 1
    else: # not in picture
        count += 1
        if len(picture) >= size:
            picture.popleft()
        picture.append([num, 1, count])
    picture = deque(sorted(picture, key=lambda x:(x[1], x[2])))
picture = sorted(picture)
for a,b,c in picture:
    print(a, end=" ")

n, m = int(input()), int(input())
frames = dict()

cnt = 0
for reco in map(int, input().split()):
    if len(frames) >= n and not reco in frames:
        del frames[min(frames, key=lambda x:frames[x])]
    try: frames[reco][0] += 1
    except:
        frames[reco] = [1, cnt]
        cnt += 1

print(*sorted(frames.keys()))

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
