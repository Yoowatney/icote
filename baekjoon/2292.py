from math import sqrt

num = int(input())
if num > 1:
    for n in range(3, int(sqrt(10**9))):
        if 3*(n - 2) * (n - 3) + 1< num <= 3*(n - 1)*(n - 2) + 1:
            print(n - 1)
            break
else:
    print(1)
