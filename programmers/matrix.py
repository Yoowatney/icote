arr1 = [[1,2], [2,3]]
arr2 = [[4,6], [7,9]]

def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for a,b in zip(arr1[i], arr2[i]):
            answer[i].append(a + b)
        # for ii in range(len(arr1[i])):
        #     answer[i].append(arr1[i][ii] + arr2[i][ii])
    return answer

print(*zip("123", "456"))

# print(solution(arr1, arr2))
# for a, b in zip(arr1[0], arr2[0]):
#     print(a,b)

# def solution(seoul):
#     return "김서방은" + str(seoul.index("Kim")) + "에 있다"

# seoul = ["Jane", "Kim"]
# print(solution(seoul))
