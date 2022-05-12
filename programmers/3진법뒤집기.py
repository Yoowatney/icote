from collections import deque
def solution(n):
    ret = deque()
    while n:
        remainder = n % 3
        ret.appendleft(remainder)
        n //= 3
    multiply = 1
    answer = 0
    for i in ret:
        answer += i * multiply
        multiply *= 3
    return answer


print(int('101', base=2))

