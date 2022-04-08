import sys
import heapq

input = sys.stdin.readline

maxheap = []
minheap = []
mx = 0
mn = 0
ret = []
for _ in range(int(input())):
    num = int(input())
    if mx <= mn:
        heapq.heappush(maxheap, [-num, num])
        mx += 1
    else:
        heapq.heappush(minheap, num)
        mn += 1
    if maxheap and minheap and maxheap[0][1] > minheap[0]:
        min = heapq.heappop(minheap)
        max = heapq.heappop(maxheap)
        heapq.heappush(minheap, max[1])
        heapq.heappush(maxheap, [-min, min])
    print(maxheap[0][1])
#     ret.append(maxheap[0][1])
# print(*ret, sep="\n")
