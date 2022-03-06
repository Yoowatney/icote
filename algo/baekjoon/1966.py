from collections import deque

for _ in range(int(input())):
    size, idx = map(int,input().split())
    
    b = [0] * size
    b[idx] = 1
    a = deque(zip(map(int, input().split()), b))
    count = 0
    while True:
        m = max(a)
        temp = a.popleft()
        if m[0] == temp[0]:
            count += 1
            if temp[1]:
                break
        else:
            a.append(temp)
    print(count)
