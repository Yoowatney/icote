# def consecutive_idx(id: str,  idx:int)->int:
#     l = len(id)
#     count = idx
#     for j in range(idx, l - 1):
#         if id[j] != id[j + 1]:
#             break
#         count += 1
#     return count
#
# def solution(new_id:str)->str:
#     answer = ""
#     new_id = new_id.lower() # lv 1
#     for i in new_id: # lv 2
#         # is alnum
#         if i in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
#             # ∑´´ååßƒƒ©©
#             answer += i
#     l = len(answer)
#     i = 0
#     idx = 0
#     ret = ""
#     while i < l: # lv 3
#         if answer[i] == '.':
#             idx = consecutive_idx(answer, i)
#             if i != idx:
#                 i = idx
#         ret += answer[i]
#         i += 1
#     # while '..' in answer:
#     #     answer = answer.replace("..", ".")
#     ret = ret.strip('.') # lv 4
#     l = len(ret)
#     if l == 0:
#         ret = 'a'
#         l = 1
#     if l >= 16:
#         ret = ret[0:15]
#         ret = ret.rstrip(".")
#     elif l <= 2:
#         for i in range(3 - l):
#             ret += ret[-1]
#     return ret
import re
def solution(dartResult):
    ret = dartResult.lower()
    print("1단계 : ",ret)
    ret = re.sub('[^a-z0-9\-_\.]', '', ret)
    print("2단계 : ",ret)
    ret = re.sub('\.+', '.', ret)
    print("3단계 : ",ret)
    ret = ret.strip('.')
    print("4단계 : ",ret)
    if not ret:
        ret = "a"
    print("5단계 : ",ret)
    if len(ret) >= 16:
        ret = ret[:15]
    ret = ret.strip('.')
    print("6단계 : ",ret)
    n = len(ret)
    if n <= 2:
        ret = ret + ret[-1] * (3 - n)
    print("7단계 : ",ret)
    return ret
