import re

def solution(s):
    p = re.compile("{([0-9,]+)}")
    n_tuple = sorted([ret.split(",") for ret in p.findall(s)], key=lambda x:len(x))
    ret = []
    for tuple in n_tuple:
        for t in tuple:
            if t not in ret:
                ret.append(t)
    return [int(i) for i in ret]

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))




