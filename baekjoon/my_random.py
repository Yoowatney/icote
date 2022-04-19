import random
num = random.randint(1, 100)
# print("선택한 숫자 : ", num)

my_num = 0
count = 0
while num != my_num:
    my_num = int(input("숫자를 입력해주세요 : "))
    count += 1
    if my_num > num:
        print(f'입력한 {my_num}보다 이하입니다')
    elif my_num < num:
        print(f'입력한 {my_num}보다 이상입니다')
    else:
        print(f'입력한 숫자 : {my_num}, 선택숫자 : {num}')
        print("총 시도한 횟수 : ", count)
        break
