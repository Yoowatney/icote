def solution(numbers):
    return sum([i for i in [0,1,2,3,4,5,6,7,8,9] if i not in numbers])

print(solution([1,2,3,4,6,7,8,0]))
