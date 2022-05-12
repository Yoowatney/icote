# def solution(s): # s는 1000개
#     answer = 0
#     increasing = 1
#     # for i in range(1, len(s)):
#     #     while 
#     #     if s[0:i] == s[i:2*i]:
#     #         
#     # s[0:1] = s[1:1+1]
#     return answer

# solution("aabbacc")


# for i in range(1, len(s)):
#     ret = ""
#     start = 0
#     end = i + 1
#     sign = 1
#     while end < len(s):
#         # print("now : ",s[start:end], s[end:end + i + 1])
#         if s[start : end] == s[end : 2 * end]:
#             ret += str(i)
#             ret += s[start : end]
#             start = end
#             end *= 2
#             sign = 0
#             # print("answer : ", s[start : end], i)
#         else:
#             ret += s[start : end]
#             # print("first start, end : ", start, end)
#             start = end
#             end = end + i + 1
#             # print("after start, end : ", start, end)
#     if sign:
#         ret += s[start : end]
#     answer.append(ret)
def solution(s):
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
        # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 다시 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        print(compressed, step)
        # 만들어지는 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
print(solution("1231234"))

# s = "aabbaccc"
#
# for i in range(1, len(s)):
#     start = 0
#     end = i # 인덱스의 크기가 문자열 압축의 길이
#     ret = ""
#     while True:
#         if s[start:end] == s[end : 2 * end]:
#             ret += str(i)
#             ret += s[start : end]
#             # start = end
#             # end += i
#             start = 2 * end
#             end = 2 * end + i
#         else:
#             ret += s[start:end]
#             start = end
#             end += i
#             # print(ret, start, end)
#         if end >= len(s):
#             ret += s[start:]
#             break
#     print("ret : ",ret)
#     # exit(0)
