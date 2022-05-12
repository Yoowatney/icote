def solution(s, n):
    answer = ''
    for i in s:
        ord_num = 0
        if i == " ":
            ord_num = 32
        elif i.isupper():
            ord_num = (ord(i) - 65 + n) % 26 + 65
        else:
            ord_num = (ord(i) - 97 + n) % 26 + 97
        answer += chr(ord_num)
    print(answer)
    return answer
    # return answer
solution('ZZz  xy', 1)
# A = 65 - > 0
# Z = 90 - > 25

# 만약 Z 가 주어지고 n이 3이 주어진다면
# 원하는 값은 C = 67

# (90 - 65 + 3) % 26 = 28 % 26 = 2

# (89 - 1 - 65 + 1) % 25 = 24 % 25
# (89 - 65 + 5) % 26 = 29 % 26 = 3
# X => Z, A, B, C, D = 68



# a = 97 - > 0
# z = 122 -> 25
