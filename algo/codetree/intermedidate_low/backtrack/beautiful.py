


# one = {"1" * i for i in range(1, n + 1)}
# two = {"22"*i for i in range(1, n // 2 + 1)}
# three = {"333"*i for i in range(1, n // 3 + 1)}
# four = {"4444" * i for i in range(1, n // 4 + 1)}
# one = one.union(two).union(three).union(four)
# print(one)



# def consecutive():
#     i = 0
#     while True:
#         n = arr[i]
#         for k in range(i, n):
#
#         for i in range(n)
#     
#
#
#     for i in range(n):
#         n = arr[i]
#         while arr[]:
#
#     return True
#     pass

n = int(input())

arr = []
count = 0


def is_beautiful():
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return False
        for j in range(i, i + arr[i] - 1):
            if arr[j] != arr[j + 1]:
                return False
        # 1 2 2 3
        # i = 1 => 3
        i += arr[i]
    return True

def count_conse(num, arr): # 연속된 숫자 갯수를 카운트 해줌
    count = 0
    ret = []
    for i in range(n):
        if arr[i] == num:
            count += 1
        else:
            ret.append(count)
            count = 0
    if count != 0:
        ret.append(count)
    return ret

# print(count_conse(2, [2, 1, 2]))

def choose(num):
    global count
    if num == n + 1:
        # printed = 1
        # for i in range(1, 5): # * 4
        #     for k in count_conse(i, arr): # N * N
        #         # if arr == [2,1,2]:
        #         #     print(i, count_conse(i, arr), k % i)
        #         # if arr.count(i) % i != 0 or k % i != 0:
        #         if k % i != 0:
        #             printed = 0
        #             break
        # if printed:
        #     count += 1

        if is_beautiful():
            # print(arr)
            count += 1
        return
    for i in range(1, 5):
        arr.append(i)
        choose(num + 1)
        arr.pop()

choose(1)
print(count)

