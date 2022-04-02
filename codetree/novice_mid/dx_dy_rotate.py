#  ============= 시계방향
dir_num = 3

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 1, 5

dir_num = (dir_num + 1) % 4
x += dx[dir_num]
y += dy[dir_num]
# print(x, y)


# ============ 반시계 방향

dir_num = 3

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 1,5
# if dir_num == 0:
#     dir_num = 3
# elif dir_num == 3:
#     dir_num = 2
# elif dir_num == 2:
#     dir_num = 1
# else: #dir_num == 1
#     dir_num = 0

dir_num = (dir_num - 1 + 4) % 4
x += dx[dir_num]
y += dy[dir_num]
print(x, y)
