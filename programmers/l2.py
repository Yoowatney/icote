

numbers = list(map(int, input().split()))



def solution(numbers):
    n = len(numbers)
    s = set()
    for i in range(n):
        for j in range(i + 1, n):
            s.add(numbers[i] + numbers[j])
    print(sorted(s))
    return sorted(s)
