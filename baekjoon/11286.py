import heapq
import sys

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, [abs(num), num])
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)
