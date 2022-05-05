def solution(n):
    # str_num = sorted(list(str(n)), reverse=True)
    # ret = ''.join(str_num)
    # return int(ret)
    return int(''.join(sorted(list(str(n)), reverse=True)))

# a.sort(reverse=True)
print(solution(12345))


a = "123"
