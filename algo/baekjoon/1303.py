from collections import deque

w, h = map(int, input().split())

war = [list(input()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
white = 0
blue = 0

# def dfs(x, y, pre_node):
#     if not 0 <= y < h or not 0 <= x < w or visited[y][x] or pre_node != war[y][x]:
#         return [0]
#     visited[y][x] = True
#     global cnt
#
#     cnt += 1
#     dfs(x - 1, y, war[y][x])
#     dfs(x + 1, y, war[y][x])
#     dfs(x, y - 1, war[y][x])
#     dfs(x, y + 1, war[y][x])
#     return [cnt, war[y][x]]

def bfs(x, y):
    if not 0 <= x < w or not 0 <= y < h or visited[y][x]:
        return 0
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    cnt = 0
    while q:
        cur_x, cur_y = q.popleft()
        cnt += 1
        for way in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            link_x = cur_x + way[0]
            link_y = cur_y + way[1]
            if 0 <= link_x < w and 0 <= link_y < h \
                    and war[link_y][link_x] == war[cur_y][cur_x] and not visited[link_y][link_x]:
                q.append((link_x, link_y))
                visited[link_y][link_x] = True
    return cnt


for x in range(w):
    for y in range(h):
        cnt = 0
        ret = bfs(x, y)
        if war[y][x] == 'W': white += ret * ret
        else: blue += ret * ret
        # ret = dfs(x, y, war[y][x])
        # if ret[0]:
        #     if ret[1] == 'W': white += ret[0] * ret[0]
        #     else: blue += ret[0] * ret[0]

print(white, blue)
