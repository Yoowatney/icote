from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        if self.dq:
            return 0
        return 1

    def size(self):
        return len(self.dq)
        
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception("Queue is emty")
        return self.dq[0]

def solution(arr):
    global q
    if arr[0] == "push":
        q.push(int(arr[1]))
    elif arr[0] == "front":
        print(q.front())
    elif arr[0] == "size":
        print(q.size())
    elif arr[0] == "empty":
        print(q.empty())
    else:
        print(q.pop())

q = Queue()

for _ in range(int(input())):
    l = input().split()
    solution(l)
