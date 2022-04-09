import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {}

for i in range(n):
    name = input().rstrip()
    s[name] = i + 1
    s[str(i + 1)] = name

for i in range(m):
    print(s[input().rstrip()])



# print(s)

#     s[input().split()]
#     arr.append(input().split())
#
# print(arr)
# print(arr[25])
