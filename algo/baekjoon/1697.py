from collections import deque

n, k = map(int, input().split())

def bfs(n, distance, k):
    distance[n] = 0
    q = deque([n])
    while (q):
        val = q.popleft()
        if val == k:
            return distance[val]
        for i in [val - 1, val + 1, val * 2]:
            if 0 <= i <= 100000 and not distance[i]:
                q.append(i)
                distance[i] = distance[val] + 1
        # if 0<= val - 1 <= 100000 and not distance[val - 1]:
        #     q.append(val - 1)
        #     distance[val - 1] = distance[val] + 1
        # if 0<= val + 1 <= 100000 and not distance[val + 1]:
        #     q.append(val + 1)
        #     distance[val + 1] = distance[val] + 1
        # if 0<= val * 2 <= 100000 and not distance[val * 2]:
        #     q.append(val * 2)
        #     distance[val * 2] = distance[val] + 1
distance = [0] * 100001
print(bfs(n, distance, k))


# 다른 사람 풀이

# import sys
# from collections import deque
# N, K = list(map(int, sys.stdin.readline().split()))
# visited = [0 for _ in range(100001)]
# visited[N] = 1
# q = deque([(N,0)])
# while True:
#     x, n = q.popleft()
#     if x == K:
#         print(n)
#         break
#     for i in -1,1,x:
#         dx = x+i
#         if dx>=0 and dx<=100000 and visited[dx]==0:
#                 q.append((dx, n+1))
#                 visited[dx]=1
