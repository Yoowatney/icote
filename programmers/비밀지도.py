# 지도는 " "공백, 또는 "#"벽 으로 이루어짐
def make_map(n, arr, answer):
    for i in range(n):
        while arr[i]:
            answer[i].append(arr[i] % 2)
            arr[i] //= 2
        remain = n - len(answer[i])
        while remain:
            answer[i].append(0)
            remain -= 1
        answer[i].reverse()

def decode(n, map, answer):
    for row in range(n):
        s = ''
        for col in range(n):
            if map[row][col] == 1:
                s += '#'
            else: s += ' '
        answer.append(s)

def solution(n, arr1, arr2):
    answer = []
    map1 = [[] for _ in range(n)]
    map2 = [[] for _ in range(n)]
    make_map(n, arr1, map1)
    make_map(n, arr2, map2)

    for row in range(n):
        for col in range(n):
            map1[row][col] = map1[row][col] | map2[row][col]
    decode(n, map1, answer)
    return answer

# print(*zip([[1,2,3],[4,5,6]], [['a','b','c',], ['d','e', 'f']]))

print(bin(3 | 5)[2:])
