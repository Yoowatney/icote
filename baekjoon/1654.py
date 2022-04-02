k, n = map(int, input().split())

l = [int(input()) for _ in range(k)]
l.sort()

start, end = 1, l[-1]

# while start <= end: # O(logN)
#     mid = (start + end) // 2 # 중간 위치
#     lines = 0 # 랜선 수
#     for i in l: # O(K)
#         lines += i // mid # 분할 된 랜선 수
#        
#     if lines >= n: # 랜선의 개수가 분기점
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)


while start <= end: # 등호...
    cnt = 0
    mid = (start + end) // 2
    for i in l:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
