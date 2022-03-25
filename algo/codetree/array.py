import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    c = input().split()
    if c[0] == "push_back":
        arr.append(int(c[1]))
    elif c[0] == "pop_back":
        arr.pop()
    elif c[0] == "size":
        print(len(arr))
    else:
        print(arr[int(c[1]) - 1])

# print(input().split())
