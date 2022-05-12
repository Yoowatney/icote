from itertools import combinations

def solution(numbers, target):
    l = len(numbers)
    answer = 0
    for i in range(l + 1): # 20
        total = sum(numbers) # 20
        minus_list = combinations(numbers, i) # 2^20 == 100만
        for elem in minus_list:
            if total - sum(elem) * 2 == target:
                answer += 1
    return answer


print(solution([4,1,2,1], 4))
