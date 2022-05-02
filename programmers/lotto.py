def solution(lotto, win_nums):
    _lotto = sorted(lotto)
    _win_nums = sorted(win_nums)
    cnt = 0
    answer = []
    for num in _lotto:
        if num in _win_nums:
            cnt += 1
    num = 7 - cnt
    if cnt == 0: # 일치하는 번호 없음
        num = 6
        answer.append(num)
    else:
        answer.append(num)
    cnt_0 = _lotto.count(0) # 0 갯수
    if cnt_0 == 0: # 0 갯수가 없을 때
        answer.append(num)
    else:
        # answer.append(7 - cnt - cnt_0)
        answer.append(num - cnt_0)
        # if num == 6:
        #     answer.append(1)
        # else:
        #     answer.append(num - cnt_0)
    answer.sort()
    return answer

print(solution([0, 0, 0, 0, 0, 0], [20, 9, 3, 45, 4, 35]))
