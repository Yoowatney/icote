build = [list(map(int, input().split())) for _ in range(int(input()))]

for i, pivot in enumerate(build):
    count = 1
    for j, x in enumerate(build):
        if pivot[0] < x[0] and pivot[1] < x[1]:
            count += 1
    build[i].append(count)

for p in build:
    print(p[2], end=' ')


# grade = 1
# for i, a in enumerate(l):
#     sign = 1
#     for j, b in enumerate(l):
#         if i == j:
#             continue
#         if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
#             pass
#         else:
#             l[i].append(grade)
#             sign = 0
#             break
#     if sign:
#         l[i].append(i + 1)
#         grade += 1
# pprint(l)
#

# build = sorted(l, key=lambda x:(x[0], x[1]), reverse=True)
#
# i = 0
# grade = 1
# for first in build:
#     i += 1
#     sign = 0
#     for second in build[i:]:
#         if first[0] > second[0] and first[1] > second[1]:
#             pass
#         else:
#             first.append(grade)
#             sign = 1
#             break
#     if sign == 0:
#         first.append(grade)
#         grade += 1
#
# pprint(build)
    

# count = 1
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if a[i][0] > a[j][0] and a[i][1] > a[j][0]:
#             a[i].append(count)
#         else:
#             a[i].append(count)
# pprint(a)
