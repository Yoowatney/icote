x = y = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dir_num = 0

for i in input():
    if i == "L":
        dir_num = (dir_num + 1) % 4
    elif i == "F":
        x += dx[dir_num]
        y += dy[dir_num]
    else: # i == "R"
        dir_num = (dir_num - 1 + 4) % 4

print(x, y)
