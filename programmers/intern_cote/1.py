BAD_1 = 81
BAD_2 = 36
VERY_BAD_1 = 151
VERY_BAD_2 = 76

MISE = 0
C_MISE = 1

def put_mask(a):
    if a >= 81 or a >= 76:
        return True
    elif a < 81 and a < 36:
        return False

def solution(atmos):
    ret = 0 # 결과값
    mask = 0 # 사용하던 마스크가 있는지 없는지
    discard = 0 # 날짜, 2가되는날 폐기
    for i in range(len(atmos)):
        # 마스크 미착용
        if atmos[i][MISE] < BAD_1 and atmos[i][C_MISE] < BAD_2:
            if mask:
                discard += 1
            continue

        # 초미세 먼지, 폐기
        elif atmos[i][MISE] >= VERY_BAD_1 and atmos[i][C_MISE] >= VERY_BAD_2:
            if mask == 1 and discard <= 1: # 마스크가 있고 날짜 유효
                pass
            else:
                ret += 1
            mask = 0
            discard = 0
        # 마스크 착용
        elif atmos[i][MISE] >= BAD_1 or atmos[i][C_MISE] >= BAD_2:
            if discard >= 2 or mask == 0: # 마스크 폐기되고 없는 상태
                ret += 1
                discard = 0
                mask = 1
            else: # 마스크가 이미 있음
                discard += 1
                mask = 1
        print(mask, discard, atmos[i], ret)
    return ret

# print(solution([[161, 80],[161, 80], [161,80], [100,20]]))
print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [120, 81], [151, 75]]	))
# print(solution([[30, 15], [80, 35]]	))
