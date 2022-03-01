#!/usr/bin/env python3

# def process():
#     a = input()
#     if (a == "0"): raise Exception("!")
#     if (a[::-1] == a): return "yes"
#     return "no"
# try:
#     while (1):
#         print(process())
# except:
#     pass

while True:
    s = input()
    if s == "0": exit(0)
    elif s == s[::-1]: print("yes")
    else: print("no")
