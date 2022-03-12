temp = []
for i in input():
    if i in "ABC": temp.append(chr(ord(i) + 23))
    else: temp.append(chr(ord(i) - 3))
print(*temp, sep="")
