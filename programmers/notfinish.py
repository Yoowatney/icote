from collections import defaultdict


def solution(participant, completion):
    d = defaultdict(int)
    for p in participant:
        d[p] += 1
    for c in completion:
        d[c] -= 1
    for key in d:
        if d[key] == 1:
            return key

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
print(solution(participant, completion))




# ==> return kiki

# a = {5 : 1, 2: 2, 3 : 3}
#
# if 1 in a:
#     print("11")
