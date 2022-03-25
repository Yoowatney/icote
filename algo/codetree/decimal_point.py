# a = 13
# b = 0.165
#
# # 하나일 경우
# print("%.4f" %a)
#
# # f string으로 작성후 뒤에 .6f 식으로 붙혀주면 된다
# print(f'{a} * {b:.6f} = {a*b:.6f}')


# print("%.1f" %25.562)



from collections import deque

a = deque(input())
b = deque(input())

n = 0
while True:
    print(a)
    a.rotate(1)
    n += 1
    if a == b:
        print(n)
        exit(0)
    elif n > len(a):
        print(-1)
        exit(0)



a.rotate(-3)
print(a)
print(b)

if a == b:
    print("Hi")

# a = input()
# b = input()
# if a != b:
#     print("false")
# else:
#     print("true")

# print(a)
