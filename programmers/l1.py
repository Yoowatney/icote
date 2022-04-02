n = int(input())

def get_primes():
    arr = [False, False] + [True] * (n - 1)
    for i in range(1, n + 1):
        if arr[i]:
            for j in range(2 * i, n + 1, i):
                arr[j] = False
    return arr

def solution(n):
    primes = get_primes()
    return primes.count(True)
# primes = get_primes()
# print(primes.count(True))
print(solution(n))


