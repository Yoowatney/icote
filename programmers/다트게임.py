# def involution(s):
#     answer = 0
#     if s == "S":
#         answer = 1
#     elif s == "D":
#         answer=  2
#     else:
#         answer = 3
#     return answer
#
# def solution(dartResult):
#     store = []
#     answer = 0
#     total = 0
#     i = 0
#     while i < len(dartResult):
#         if dartResult[i].isdecimal(): # 10일때 예외처리
#             if dartResult[i + 1] == '0':
#                 i += 1
#                 answer = 10 ** (involution(dartResult[i + 1]))
#             else:
#                 answer = int(dartResult[i]) ** (involution(dartResult[i + 1]))
#             store.append(answer)
#         if i + 2 >= len(dartResult):
#             break
#         i += 2
#         if dartResult[i] == '*':
#             store[-1] *= 2
#             if len(store) >= 2:
#                 store[-2] *= 2
#             i += 1
#         elif dartResult[i] == '#':
#             store[-1] *= -1
#             i += 1
#     return sum(store)

import re
def solution(dartResult):
    involution = {"S" : 1, "D" : 2, "T" : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    # ret = re.findall('(\d+)(\w)(\*|\#?)', dartResult)
    ret = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    answer = []
    for num, i, opt in ret:
        if opt == '*' and answer:
            answer[-1] *= 2
        answer.append(int(num) ** involution[i] * option[opt])
    print(ret)
    return sum(answer)



solution("1S*2T*3S*")

# print(re.findall("\d{0,4}-(\d{2})-(\d{2})", '2028-07-28'))

# answer = []
# answer[-1] = answer[-1] * 2 if answer else []
# print(answer)
# TODO 삼항연산자에 대입 관련해 정리

# p = re.compile('([0-9])([SDT])(*#?)')
# print(re.findall('(\d)(\w)(\*|\#?)', "1S#2D*3T"))

# TODO 캡쳐는 \d와 같은 정규식에서만 가능한건지?
