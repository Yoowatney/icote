from functools import cmp_to_key

# def compare(a, b):
#     return (int(str(a) + str(b)) - int(str(b) + str(a)))
#
# def my_cmp(a, b):
#     str_a = str(a)
#     str_b = str(b) 
#     if str_a[0] == str_b[0]: 
#         if str_a[1:] == "":  # len a < len b
#             for i in str_b: 
#                 if str_a[0] < i:
#                     return 1
#                 elif str_a[0] > i:
#                     return -1
#             return 0
#         elif str_b[1:] == "":
#             for i in str_a:
#                 if str_b[0] < i:
#                     return -1
#                 elif str_b[0] > i:
#                     return 1
#             return 0
#         return my_cmp(int(str_a[1:]), int(str_b[1:]))
#     elif str_a[0] < str_b[0]:
#         return 1
#     else:
#         return -1
# def solution(numbers):
#     numbers.sort(key=cmp_to_key(my_cmp))
#     return "".join(str(i) for i in numbers)


from functools import cmp_to_key

def solution(numbers):
    def Compare_Method(a, b):
        maxLen = len(a) if len(a) <= len(b) else len(b)
        aLen = len(a)
        bLen = len(b)
        for i in range(maxLen):
            aChr = a[i] if i < aLen else a[aLen - 1]
            bChr = b[i] if i < bLen else b[bLen - 1]
            print(aChr, bChr)
            if aChr > bChr:
                return 1
            elif aChr < bChr:
                return -1
        first = str(a) + str(b) # a > b : 1
        second = str(b) + str(a)
        for i in range(len(first)):
            if first[i] < second[i]:
                return -1
            elif first[i] > second[i]:
                return 1
        return 0

        # if aLen <= bLen:
        #     if a[0] >= b[bLen - 1]:
        #         return 1
        #     else:
        #         return -1
        # else:
        #     if b[0] >= a[bLen - 1]:
        #         return -1
        #     else:
        #         return 1
    numbers = list(map(str, numbers))
    return (str(int("".join(sorted(numbers, key=cmp_to_key(Compare_Method),reverse=True)))))

a = [50,501]
# a.sort(key=cmp_to_key(compare), reverse=True)
print(solution(a))




# for num in a:
#     for i in str(num): 
#         print(i)
#
# a.sort(key=cmp_to_key(compare))
# print(a)

# mylist = [
#     'A',
#     'AA',
#     'AAA',
#     'BBB',
#     'CCC',
# ]
#
# def mycmp(x, y):
#     if len(x) > len(y):
#         return -1
#     elif len(x) < len(y):
#         return 1
#     else:
#         if x > y:
#             return 1
#         else:
#             return -1
#
# mylist.sort(key=cmp_to_key(mycmp))
# print(mylist)
# a.sort(key=cmp_to_key(my_cmp))
