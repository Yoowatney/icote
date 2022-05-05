def consecutive_idx(id: str,  idx:int)->int:
    l = len(id)
    count = idx
    for j in range(idx, l - 1):
        if id[j] != id[j + 1]:
            break
        count += 1
    return count

def solution(new_id:str)->str:
    answer = ""
    new_id = new_id.lower() # lv 1
    for i in new_id: # lv 2
        # is alnum
        if i in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            # ∑´´ååßƒƒ©©
            answer += i
    l = len(answer)
    i = 0
    idx = 0
    ret = ""
    while i < l: # lv 3
        if answer[i] == '.':
            idx = consecutive_idx(answer, i)
            if i != idx:
                i = idx
        ret += answer[i]
        i += 1
    # while '..' in answer:
    #     answer = answer.replace("..", ".")
    ret = ret.strip('.') # lv 4
    l = len(ret)
    if l == 0:
        ret = 'a'
        l = 1
    if l >= 16:
        ret = ret[0:15]
        ret = ret.rstrip(".")
    elif l <= 2:
        for i in range(3 - l):
            ret += ret[-1]
    return ret

a = "=.="

# for i in range(2):
#     a += a[-1] 
# a = ""
# print(a.strip('.'))
# print(solution(a))

print("œ".isalpha())

# print(a)


# print(consecutive_idx(a, 3))
# print(a.replace(a[3:7], '.'))
# print(a)



# a = "a...b.c.d.e.f"
# while '..' in a:
#         a = a.replace('..', '.')
#         print(a)
# print(a)
