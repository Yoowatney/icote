from collections import deque
import sys
input = sys.stdin.readline

def implement_command(command, arr):
    q = deque(arr)
    r = 0
    for i in command: # 100000
        if i == 'R' and r == 0:
            r = 1
        elif i == 'R' and r == 1:
            r = 0
        else: #D
            if q and r == 0:
                q.popleft()
            elif q and r == 1:
                q.pop()
            else:
                return False
    if r == 1:
        q.reverse()
        return q
    return q

for _ in range(int(input())):
    command = input().rstrip() # 100000
    n = int(input())
    arr = input().rstrip() # # 100000
    if arr != '[]':
        arr = list(map(int, arr[1:-1].split(',')))
    else: arr = []
    ret = implement_command(command, arr)
    if ret == False:
        print("error")
    else:
        print("[", end="")
        print(*list(ret), sep=",",end="")
        print("]")
