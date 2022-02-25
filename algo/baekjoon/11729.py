dp = [0] * 21
dp[0] = 0
dp[1] = 1

def hanoi(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = 2 * hanoi(n - 1) + 1
    return dp[n]

def move(n, start, to):
    print(start, to)
    # print(f'{n}번쨰 원반을 {start}에서 {to}로 이동')

def hanoi2(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi2(n - 1, start, via, to)
        move(n, start, to)
        hanoi2(n - 1, via, to, start)

# print(hanoi(3))
n = int(input())
print(hanoi(n))
hanoi2(n, 1, 3, 2)
# print(dp)

