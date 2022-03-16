from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur_node = q.popleft()
        print(cur_node, end=" ")
        for link_node in graph[cur_node]:
            if not visited[link_node]:
                q.append(link_node)
                visited[link_node] = True
# O(n + logn)
graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
        ]
visited = [False] * 9
# bfs(1)


q = deque()
q.append([1,2])
q.append([3,4])
print(q)
