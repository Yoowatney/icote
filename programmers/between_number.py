def sum_between_number(a, b):
    if b < a:
        a, b = b, a
    ret = 0
    for i in range(a, b + 1):
        ret += i
    return ret

print(sum_between_number(3, 5))
