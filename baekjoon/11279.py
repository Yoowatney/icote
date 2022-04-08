import heapq
import sys

heap = []
input = sys.stdin.readline
for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, [-num, num])
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)
