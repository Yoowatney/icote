
int(input())
l = list(map(int, input().split()))
s_l = sorted(set(l)) # nlogn

d = dict()
for i in range(len(s_l)):
    d[s_l[i]] = i
for i in range(len(l)):
    l[i] = d[l[i]]

print(*l)

# d = {s[0] : 1, s[1] : 2, s[2]: 3}
# print(d)
#
# for i in sorted_l:
#
#     if i == 

