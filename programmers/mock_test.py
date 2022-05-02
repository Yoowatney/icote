DIVIDE_1 = 5
DIVIDE_2 = 8
DIVIDE_3 = 10

def solution(answers):
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i in range(len(answers)):
        if math_1[i % DIVIDE_1] == answers[i]:
            count_1 += 1
        if math_2[i % DIVIDE_2] == answers[i]:
            count_2 += 1
        if math_3[i % DIVIDE_3] == answers[i]:
            count_3 += 1
    answer = [count_1, count_2, count_3]
    return [i + 1 for i in range(len(answer)) if answer[i] == max(answer)]

print(solution([1,2,3,4,5]))


# 1 2 3 4 5             5개 기준
# 2 1 2 3 2 4 2 5            8개 기준
# 3 3 1 1 2 2 4 4 5 5            10개 기준



# a = [2,2,2]
# print([i+1 for i in range(len(a)) if a[i] == max(a)])
