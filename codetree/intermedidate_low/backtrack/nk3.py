from collections import OrderedDict
from time import time
start_time = time()

n, m = tuple(map(int, input().split()))
arr = OrderedDict()

def choose(num : int) -> None:
    ''' num : 현재 인덱스, cnt : 1의 갯수
    num번째에서 원소를 집어넣어주는 함수
    '''
    if num == m + 1:
        print(*arr.keys()) # O(N)
        return
    for i in range(1, n + 1): # O(N)
        if num == 1 or i not in arr: # O(N * N)
            # 여기서부터 하면 됨
            # arr = arr.fromkeys(i)
            arr[i] = True
            # arr.add(i) # TODO O(N * N * N!) 이거 시간복잡도 이렇게 계산하는거맞음?
            # print("=== ===")
            # print(arr)
            choose(num + 1)
            arr.pop(i)
            # arr.remove(i)
choose(1)

end_time = time()
print(end_time - start_time)
