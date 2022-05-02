def solution(n):
    str_num = sorted(list(str(n)), reverse=True)
    ret = ''.join(str_num)
    return int(ret)


# a.sort(reverse=True)
print(solution(12345))
