def solution(number):
    n = len(number)
    answer = (n - 4) * '*'
    answer += number[n - 4:]
    return answer

print(solution("1234"))
