from itertools import combinations
from math import lcm

arr = list(map(int, input().split()))
# for num in range(1, 1000000):
#     for a,b,c in list(combinations([0,1,2,3,4], 3)):
#         if num % arr[a] == 0 and num % arr[b] == 0 and num % arr[c] == 0:
#             print(num)
#             exit(0)


m = 1000000
for a,b,c in list(combinations([0,1,2,3,4], 3)):
    m = min(m, lcm(arr[a], arr[b], arr[c]))
print(m)


from itertools import combinations
from math import lcm
m = 1000000
for a,b,c in list(combinations([0,1,2,3,4], 3)):
    m = min(m, lcm(arr[a], arr[b], arr[c]))
print(m)

