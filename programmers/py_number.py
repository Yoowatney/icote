def solution(s:str) -> bool:
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    if p == y:
        return True
    return False


print(solution("asd"))
