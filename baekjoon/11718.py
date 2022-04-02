import sys

input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s == "":
        exit(0)
    print(s)
