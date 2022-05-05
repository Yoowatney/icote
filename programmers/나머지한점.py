def solution(v):
    answer = []
    x = 0
    y = 0
    for a,b in v: # v= [ [1,4] , ... , [3,10]]
        x ^= a
        y ^= b
        # x.append(a)
        # y.append(b)
    return [x, y]
    answer.append(x[0]^x[1]^x[2])
    answer.append(y[0]^y[1]^y[2])
    d = [[], []]
    for a,b in v:
        d[0].append(a)
        d[1].append(b)
    d[0].sort()
    d[1].sort()
    if d[0].count(d[0][0]) == 1:
        answer.append(d[0][0])
    else:
        answer.append(d[0][2])
    if d[1].count(d[1][0]) == 1:
        answer.append(d[1][0])
    else:
        answer.append(d[1][2])
    return answer


# for a, b in [[1, 4], [3, 4], [3, 10]]:
#     print(a,b)
print(solution([[0, 0], [2, 2], [0, 2]]))

x = 1
y = 1
z = 2
print(x^y^z)

x = 0b0111
y = 0b1101
print(x^y)
x = 0x0111
x = 0o011
print(x)
