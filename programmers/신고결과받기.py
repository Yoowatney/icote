def solution(id_list, report, k):
    answer = []
    report_count = dict()
    report_list = dict()
    for id in id_list:
        report_count[id] = 0 # {'muzi' : 0 , ...}
        report_list[id] = [] # {'muzi' : [], ...}
    for rep in set(report):
        reporter, reported = rep.split() # a에는 신고횟수에 대한 정보가 담겨있음
        report_count[reported] += 1 # {'muzi' : 2, ...}
        report_list[reporter].append(reported) # {'muzi' : ['neo', 'frodo']}
    for key, value in report_list.items():
        count = 0
        for i in range(len(value)):
            if report_count[value[i]] >= k:
                count += 1
        answer.append(count)
    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))
