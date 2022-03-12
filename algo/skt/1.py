# from collections import defaultdict


money = int(input())
costs = list(map(int, input().split()))


def solution(money, costs):
    a = dict()
    money_list = [1, 5, 10, 50, 100, 500]
    i = 0

    for m in money_list:
        a[m] = costs[i]
        i += 1

    if a[500] > a[100] * 5:
        del a[500]
    if a[100] > a[50] * 2:
        del a[100]
    if a[50] > a[10] * 5:
        del a[50]
    if a[10] > a[5] * 2:
        del a[10]
    if a[5] > a[1] * 5:
        del a[5]

    changes = sorted(a.keys(), reverse=True)
    answer = 0
    for change in changes:
        answer += a[change] * (money // change)
        money = money % change
    return answer

print(solution(money, costs))


# a = defaultdict(int)
# a = dict()
#
# a[1] = costs[0] # 자동화 나중에 ㄱㄱ
# a[5] = costs[1]
# a[10] = costs[2]
# a[50] = costs[3]
# a[100] = costs[4]
# a[500] = costs[5]
#
# if a[500] > a[100] * 5:
#     del a[500]
# if a[100] > a[50] * 2:
#     del a[100]
# if a[50] > a[10] * 5:
#     del a[50]
# if a[10] > a[5] * 2:
#     del a[10]
# if a[5] > a[1] * 5:
#     del a[5]
#
#
# changes = sorted(a.keys(), reverse=True)
# print(changes)
#
#
# res = 0
# for change in changes:
#     res += a[change] * (money // change)
#     money = money % change
# print(res)

