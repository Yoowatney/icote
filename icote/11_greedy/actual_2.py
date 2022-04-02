n,m,k = map(int, input().split())
l = sorted((map(int, input().split())), reverse=True)
print(l)

count = 0
result = 0
for i in range(m):
    if count == k:
        result += l[1]
        count = 0
        continue
    result += l[0]
    count += 1
print(result)
