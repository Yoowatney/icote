from itertools import combinations
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(nums):
    count = 0
    for comb in combinations(nums, 3):
        count += is_prime(sum(comb))
    return count

print(solution([1,2,7,6,4]))
