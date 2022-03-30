# arr = [1,2,3,4, 2, 2]
# print(arr.count(2))
# print(''.join(str(i) for i in arr))


arr = [1,2, 1, 2]

def countlist(random_list):
    retlist = []
    count = 0
    # Avoid IndexError for  random_list[i+1]
    for i in range(len(random_list) - 1):
        # Check if the next number is consecutive
        if random_list[i] + 1 == random_list[i+1]:
            count += 1
        else:
            # If it is not append the count and restart counting
            retlist.append(count)
            count = 1
    # Since we stopped the loop one early append the last count
    retlist.append(count)
    return retlist

# def count_cosec(num):
#     for i in range

print(countlist([1,4,5,6,7,9,19,21,22,23,24]))




print(*range(0, 5))


