
def solution(d, budget):
    answer = 0
    total = 0
    d = sorted(d)
    for i in d:
        if total + i <= budget:
            total += i
            answer += 1
        else:
            return answer

        # else:
        #     break
    # return answer

print(solution([1,3,2,5,4], 9))


# for x in range(4):
#     if x == 2:
#         print('loop out')
#         break
# else:
#     print("loop end")
