def solution(dir, n):
    global x, y
    i = directions[dir]
    x += dx[i] * n
    y += dy[i] * n
x = y = 0
directions = {
        "N" : 0,
        "E" : 1,
        "W" : 2,
        "S" : 3
        }

# directions = ["N", "E", "W", "S"]
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
for _ in range(int(input())):
    a, b = input().split()
    solution(a, int(b))
print(x, y)
