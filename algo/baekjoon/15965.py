# def get_prime_list():

sieve = [False, False] + [True] * 10000000
for i in range(2, int(10000000 ** 0.5) + 1):
    if sieve[i]:
        for k in range(2 * i, 10000000, i):
            sieve[k] = False
li = [i for i in range(2, 10000000) if sieve[i]]
print(li[int(input()) - 1])
# print(primes[int(input()) - 1])
