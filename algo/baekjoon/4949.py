while True:
    l = []
    s = input()
    if s == ".":
        break
    for i in s:
        if i == "(" or i == "[":
            l.append(i)
        elif i == ")" or i == "]":
            if l and l[-1] == "(" and i == ")":
                l.pop()
            elif l and l[-1] == "[" and i == "]":
                l.pop()
            elif not l or (l[-1] == "[" and i == ")") or (l[-1] == "(" and i == "]"):
                l = [1]
                break
    if not l: print("yes")
    else:  print("no")
