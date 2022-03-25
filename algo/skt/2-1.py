from pprint import pprint
goods = ["pencil", "cilicon", "contrabase", "picturelist"]
goods = ["abcdeabcd","cdabe","abce","bcdeab"]

n = len(goods)
temp = [[] for _ in range(n)]
idx = 0
for pivot in goods:
    n = len(pivot)
    i = 0
    end = 1
    j = end
    while True:
        sign = 0
        l = 0
        for comp in goods:
            if pivot != comp and pivot[i:j] not in comp:
                l = len(pivot)
                sign += 1
        if sign == 3:
            if temp[idx] and len(temp[idx][-1]) != len(pivot[i:j]):
                break
            temp[idx].append(pivot[i:j])
            i += 1
            j += 1
        else:
            i += 1
            j += 1
            if i == l:
                i = 0
                end += 1
                j = end
    idx += 1
# for i in range(n):
#     temp[i] = [set(temp[i])]
pprint(temp)
n = len(goods)
for i in range(n):
    temp[i] = list(set(temp[i]))
# temp[0] = list(set(temp[0]))
# temp[1] = list(set(temp[1]))
# temp[2] = list(set(temp[2]))
# temp[3] = list(set(temp[3]))
pprint(temp)
            
    # for i in range(n):
        # j = i
        # sign = 0
        # for comp in goods:
        #     if pivot != comp and pivot[i] not in comp:
        #         # print(comp, pivot[i])
        #         sign += 1
        # if sign == 3:
        #     print(pivot[i])
        #     print(pivot)
        #     exit(0)
