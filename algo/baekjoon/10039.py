a = []
for _ in range(5):
    score = int(input())
    a.append(score) if score >= 40 else a.append(40)
print(sum(a) // 5)
