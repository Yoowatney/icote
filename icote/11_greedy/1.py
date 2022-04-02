n = int(input())

l = sorted(map(int, input().split()))
result = 0
for i in range(0, len(l)):
    if l[i] != -1 and max(l[i : i + l[i]]) <= len(l[i : i + l[i]]):
        l[i : i + l[i]] = [-1 for _ in range(i, i + l[i])]
        result += 1
print(result)

count = 0
for i in l:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
