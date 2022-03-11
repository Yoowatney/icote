
# def solutuon()

n, m = map(int, input().split()) # 100만, 20억

rice = sorted(list(map(int, input().split())))
print(rice)


start = 0
end = rice[-1]

while start <= end: # 떡길이
    cnt = 0
    mid = (start + end) // 2
    for i in rice: # O(N)
        cnt += i % mid if i > mid else 0
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
