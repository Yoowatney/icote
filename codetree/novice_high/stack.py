import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return 0 if self.items else 1

    def size(self):
        return len(self.items)
 
    def pop(self):
        assert self.empty() == 0, "이런 경우는 존재하지 않습니다."
        return self.items.pop()

    def top(self):
        assert self.empty() == 0, "이런 경우는 존재하지 않습니다."
        return self.items[-1] 

def solution(arr):
    if arr[0] == "push":
        s.push(int(arr[1]))
        pass
    elif arr[0] == "pop":
        print(s.pop())
        pass
    elif arr[0] == "size":
        print(s.size())
        pass
    elif arr[0] == "empty":
        print(s.empty())
        pass
    else:
        print(s.top())

s = Stack()
for _ in range(int(input())):
    solution(input().split())
