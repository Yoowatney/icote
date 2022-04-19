n = int(input())
arr = list(map(int, input().split()))
temp_arr = arr[::]
l = len(str(max(arr)))

for idx in range(1, l + 1):
    temp = [[] for _ in range(10)]
    for elem in arr:
        if len(str(elem)) < idx:
            temp[0].append(elem)
            continue
        temp[int(str(elem)[-idx])].append(elem)
    arr = []
    for i in range(10):
        for j in range(len(temp[i])):
            arr.append(temp[i][j])
print(*arr)
