def solution(rooms, target):
    d = {}
    for room in rooms:
        idx = 0
        num = ""
        people = []
        for i in range(len(room)):
            if room[i].isdecimal():
                num += room[i]
            if room[i] == "]":
                people = room[i + 1:].split(",")
        num = int(num)
        d[num] = []
        for p in people:
            d[num].append(p)
        # if d[target]:
    del d[target]
    print(d)
    answer = []
    return answer

rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
print(solution(rooms, 403))
# for room in rooms:
#     num = ""
#     people = []
#     d = {}
#     for i in range(len(room)):
#         if room[i].isdecimal():
#             num += room[i]
#         if room[i] == "]":
#             people = room[i + 1:].split(",")
#     num = int(num)
#     d[num] = []
#     for p in people:
#         d[num].append(p)
    # d[num] = "Heelo"
    # print(people)
    # print(num)

    # for i in room:
    #     if i.isdecimal():
    #         num += i
    # num = int(num)
    # print(num)
    # exit(0)
