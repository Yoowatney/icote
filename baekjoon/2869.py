a,b,v = map(int, input().split())

val = (v - a) / (a - b)
print(int(val + 2) if val - int(val) else int(val + 1))
