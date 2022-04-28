def solution(n):
    pivot = 2
    while True:
        if n % pivot == 1:
            return pivot
        pivot += 1
print(solution(12))
