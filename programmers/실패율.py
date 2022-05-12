from collections import Counter, deque

def solution(N, stages):
    count = sorted(Counter(stages).items())
    n = len(stages)
    fractions = [0 for _ in range(N)]
    # fractions = [[0] for _ in range(N)]

    # rafactoring
    idx = 0
    for key, value in count:
        if key > N:
            break
        # fractions[idx].append(value / n)
        # fractions[idx].append(key)
        fractions[key - 1] = value / n
        n = n - value
        idx += 1
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

# print(solution(4, [4,4,4,4,4]))
def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

# a = [1,2,3,4]
# while len(a):
#     print(a)
#     a.pop()

a = [1,2,1,1]
print(a.count(1))

# solution(4, [4,4,4,4,4])
# for a, b in enumerate([1,2,3]):
#     print(a,b)


# a = [0,1,2]
# a[0] = 3/5
# print(a)
