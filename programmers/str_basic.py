def solution(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    return False

a = "1234577"
print(solution(a))
