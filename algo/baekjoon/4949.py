# while True:
#     l = []
#     s = input()
#     if s == ".":
#         break
#     for i in s:
#         if i == "(" or i == "[":
#             l.append(i)
#         elif i == ")" or i == "]":
#             if l and l[-1] == "(" and i == ")":
#                 l.pop()
#             elif l and l[-1] == "[" and i == "]":
#                 l.pop()
#             elif not l or (l[-1] == "[" and i == ")") or (l[-1] == "(" and i == "]"):
#                 l = [1]
#                 break
#     if not l: print("yes")
#     else:  print("no")






while True:
    a = []
    str = input()
    if str == ".": break
    try:
        for s in str:
            if not s in ["[", "]", "(", ")"]:
                continue
            elif s == "(":
                a.append("(")
            elif s == "[":
                a.append("[")
            elif s == "]" and a[-1] == "(":
                raise Exception("!")
            elif s == ")" and a[-1] == "[":
                raise Exception("!")
            else:
                a.pop()
            # elif s == "]" and a[-1] == "[":
            #     a.pop()
            # elif s == ")" and a[-1] == "(":
                # a.pop()
    except:# Exception as e:
        a = [1]
    if a: print("no")
    else: print("yes")
