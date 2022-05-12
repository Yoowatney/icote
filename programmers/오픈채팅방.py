def solution(record):
    user = {}
    command = []
    answer = []
    for r in record:
        a, b, c = 0, 0, 0
        try:
            a, b, c = r.split(" ")
        except:
            a, b = r.split(" ")
        if a == "Change":
            user[b] = c
        elif a == "Enter":
            user[b] = c
        command.append([a, b])
    print(user)
    for c, id in command:
        if c == "Enter":
            answer.append(f"{user[id]}님이 들어왔습니다.")
        elif c == "Leave":
            answer.append(f"{user[id]}님이 나갔습니다.")
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Enter uid3333 Muzi", "Change uid3333 Off","Leave uid3333 Muzi"]
# 무지 입장 = 프로도입장
# 프로도 입장 라이언 입장
# 무지 떠남 프로도 떠남
# 



# record = ["Enter uid1 Muzi", "Change uid1 Error","Leave uid1 Muzi"]

print(solution(record))

# b = "Hi!"
# a = []
# a.append(f"{b}님이 들어옴")
# print(a)
