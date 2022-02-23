import sys
input = sys.stdin.readline

prime_list = [False, False] + [True] * 10002

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2 * i, 10002, i):
            prime_list[j] = False

for i in range(int(input())):
    n = int(input())
    a = n // 2
    b = a
    while a:
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1



def get_primes(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            # i가 소수인 경우
            for j in range(i+i, n, i):
                # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


def prime(n):
    for i in range(2, int(n ** 1/2) + 1):
        if (n % i == 0):
            return 0
    return 1

def get_partition(n):
    temp = 500000
    ret_j = 0
    ret_i = 0
    for i in primes:
        if i > n:
            break
        if n - i > 1 and prime(n - i) and temp > abs(n - 2 * i):
            temp = abs(n - 2 * i)
            ret_i = i
            ret_j = n - i
           
    # for i in primes:
    #     for j in primes:
    #         if i + j == n and temp > abs(j - i):
    #             temp = abs(j - i)
    #             ret_j = j
    #             ret_i = i
    return sorted([ret_i, ret_j])




l = [int(input()) for _ in range(int(input()))]
primes = get_primes(sorted(l, reverse=True)[0])

for n in l:
    print(*get_partition(n))


# for num in range(5, m):
#     prime = 1
#     for i in range(2, num):
#         if num % i == 0:
#             prime = 0
#             break
#     if prime:
#         p_list.append(num)
# print(p_list)
