from collections import deque

def solution(arr):
    global q
    if arr[0] == "push_back":
        q.append(int(arr[1]))
    elif arr[0] == "push_front":
        q.appendleft(int(arr[1]))
    elif arr[0] == "pop_front":
        print(q.popleft())
    elif arr[0] == "pop_back":
        print(q.pop())
    elif arr[0] == "empty":
        if q: print(0)
        else: print(1)
    elif arr[0] == "size":
        print(len(q))
    elif arr[0] == "front":
        print(q[0])
    else:
        print(q[-1])

q = deque()
for _ in range(int(input())):
    l = input().split()
    solution(l)
