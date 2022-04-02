while True:
    a = [input() for _ in range(int(input()))]
    if a == []:
        break
    a.sort(key=lambda x:x.lower())
    print(a[0])
