def solution(x, n):
    initial = x
    answer = []
    for _ in range(n):
        answer.append(initial)
        initial += x
    return answer

x, n = 2, 5

print(solution(x, n))
