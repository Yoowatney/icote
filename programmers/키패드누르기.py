def solution(numbers, hand):
    answer = ''
    left_x, left_y = 9 // 3, 9 % 3
    right_x, right_y = 11 // 3, 11 % 3
    for num in numbers:
        if num == 0:
            num = 11
        if num in [1, 4, 7]:
            answer += 'L'
            left_x, left_y = (num - 1) // 3, (num - 1) % 3
        elif num in [3, 6, 9]:
            answer += 'R'
            right_x, right_y = (num - 1) // 3, (num - 1) % 3
        else:
            x, y = (num - 1) // 3, (num - 1) % 3
            left = abs(left_x - x) + abs(left_y - y)
            right = abs(right_x - x)**2 + abs(right_y - y)**2
            if left < right:
                answer += 'L'
                left_x, left_y = (num - 1) // 3, (num - 1) % 3
            elif left > right:
                answer += 'R'
                right_x, right_y = (num - 1) // 3, (num - 1) % 3
            elif hand == 'left':
                answer += 'L'
                left_x, left_y = (num - 1) // 3, (num - 1) % 3
            else:
                answer += 'R'
                right_x, right_y = (num - 1) // 3, (num - 1) % 3
    return answer
        # [2,5,8,0] 엄지 위치를 고려해줘야함

        # else:
        # if num == 0:
        #     num = 11
        # num -= 1
        # x, y = num // 3, num % 3
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([1,3,9,5], "left"))





from collections import deque
# * = 10
# 0 = 11
# # = 12

# 아래는 문제 잘못읽고 풀었습니다...
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]
def is_range(x, y):
    if 0 <= x < 3 and 0 <= y < 4:
        return True

def bfs(x, y, distances, aim_x, aim_y):
    q = deque()
    q.append([x,y])
    distances[y][x] = 1
    while q:
        linked_x, linked_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + linked_x, dy + linked_y
            if is_range(nx, ny) and distances[ny][nx] == 0:
                distances[ny][nx] = distances[linked_y][linked_x] + 1
                q.append([nx, ny])
    return distances[aim_y][aim_x] - 1

def wrong_solution(numbers, hand):
    answer = ''
    left_x, left_y = 9 % 3, 9 // 3
    right_x, right_y = 11 % 3, 11 // 3

    for num in numbers:
        if num == 0:
            num = 11
        num = num - 1
        x, y = num % 3, num // 3 # 누를 위치
        print(left_x, left_y, right_x, right_y)
        # left_x, left_y = left % 3, left // 3
        # right_x, right_y = right % 3, right // 3

        # print(left_x, left_y)
        # print(right_x, right_y)
        # print(x, y)

        # 왼쪽에서 잰 거리
        distances = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
        left_result = bfs(left_x, left_y, distances, x, y)
        # for i in distances:
        #     print(i)
        # print()
        # 오른쪽에서 잰 거리
        distances = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
        right_result = bfs(right_x, right_y, distances, x, y)
        # for i in distances:
        #     print(i)
        if left_result < right_result:
            answer += 'L'
            left_x, left_y = x, y # 갱신
        elif left_result > right_result:
            answer += 'R'
            right_x, right_y = x, y
        elif hand == 'left':
            answer += 'L'
            left_x, left_y = x, y # 갱신
        else:
            answer += 'R'
            right_x, right_y = x, y
    return answer
        # bfs(x, y, distances)
