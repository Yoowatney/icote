
from collections import Counter

def solution(nums):
    answer = 0
    num = len(nums)
    poncket_nums = len(Counter(nums).keys())
    if poncket_nums >= num // 2:
        answer = num // 2
    else:
        answer = poncket_nums

    return answer

print(solution([3,3,3,2,2,2]))
