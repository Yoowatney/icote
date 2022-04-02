def determine(arr):
    stack = []
    for i in arr:
        if i == "(":
            stack.append('(')
        else:
            if stack: stack.pop()
            else: return False
    if stack: return False
    return True

if not determine(input()):
    print("No")
else:
    print("Yes")
