from collections import Counter, deque

def solution(N, stages):
    count = sorted(Counter(stages).items())
    n = len(stages)
    fractions = [0 for _ in range(N)]
    # rafactoring
    for key, value in count:
        if key > N:
            break
        fractions[key - 1] = value / n
        n = n - value
    order_fractions = sorted(fractions)
    answer = []
    
    while True:
        for i in range(len(fractions)):
            if fractions[i] == order_fractions[-1]:
                answer.append(i + 1)
                fractions[i] = -1
                order_fractions.pop()
                break
        if fractions.count(-1) == N:
            break
    return answer

print(sorted(Counter([1,1,3,4,5,6,1,3]).items()))
# solution(4, [4,4,4,4,4])
# for a, b in enumerate([1,2,3]):
#     print(a,b)


# a = [0,1,2]
# a[0] = 3/5
# print(a)
