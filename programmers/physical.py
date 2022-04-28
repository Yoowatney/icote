def solution(n, lost, reserve):
    # reserve.sort()
    r = set(reserve)
    l = set(lost)
    reserve = r - l
    lost = l - r
    # reserve = [r for r in reserve if r not in lost]
    # lost = [l for l in lost if l not in reserve]
    cloth = [i + 1 for i in range(n) if i + 1 not in lost] # 옷을 들고있는 학생수 for i in range(len(lost)):
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
            cloth.append(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
            cloth.append(r + 1)
    return len(cloth)

# print(solution(5, [], [2]))

reserve = [1,2,3]
lost = [3, 4]
r = set(reserve)
l = set(lost)
print(l - r)
# reserve = [r for r in reserve if r not in lost]
# print(reserve)
# a = [1,2,3]
# a = [i for i in a if i != 1]
# print(a)
