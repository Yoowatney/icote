# from collections import Counter
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# nl = list(map(int, input().split()))
# c = Counter(nl)
# m = int(input())
# for i in list(map(int, input().split())):
#     print(c[i], end=" ")

from collections import defaultdict

d = defaultdict(int)

print(d)
print(d[5])
d[0] += 1
print(d)
print(d[0])




