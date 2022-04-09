import sys
input = sys.stdin.readline

n = int(input())

arr = [0]
for i in map(int, input().split()):
    arr.append(i)

for i in range(2, n + 1):
    arr[i] = max([arr[i - k] + arr[k] for k in range(0, (n // 2) + 2) if i - k >= 0])
print(arr[-1])
