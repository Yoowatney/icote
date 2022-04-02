from time import time
start_time = time()
n, m = tuple(map(int, input().split()))

arr = []

def choose(num : int) -> None:
    '''
    num : 현재 인덱스 + 1
    num번째에서 원소를 집어넣어주는 함수
    '''
    if num == m + 1:
        print(*arr) # O(N)
        return
    for i in range(1, n + 1):
        if num == 1 or i not in arr:
            arr.append(i)
            choose(num + 1)
            arr.pop()
choose(1)

end_time = time()
print(end_time - start_time)
