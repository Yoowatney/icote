#!/usr/bin/env python3

# def process(person, k):
#     ret = []
#     while person:
#         if (len(person) > k):
#             ret.append(person[k - 1])
#             person.remove(person[k - 1])
#             person = person[k - 1:] + person[:k - 1]
#         else:
#             idx = k % len(person) - 1
#             ret.append(person[idx])
#             person.remove(person[idx])
#             if (idx != -1):
#                 person = person[idx:] + person[:idx]
#     return (ret)
# n, k = map(int, input().split())
#
# person = list(range(1, n + 1))
# print('<', end='')
# print(*process(person, k), sep=', ', end='')
# print('>', end='')

from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n+1))
ans = list()
while len(dq):
    dq.rotate(-k+1)
    ans.append(dq.popleft())
print(f"<{str(ans)[1:-1]}>")

# a = [1,2,3,4,5,6,7]
# a = a[3:] + a[0:2]
# print(a)
