def solution(id_list, report, k):
    answer = []
    report_user = []
    banned = []
    dic = {}
    for i in id_list:
        dic[i] = []
        
    for g in list(set(report)):
        dic[g.split(" ")[0]].append(g.split(" ")[1])
        report_user.append(g.split(" ")[1])
    
    for l in id_list :
        if report_user.count(l) >= k:
            banned.append(l)
    
    for m in id_list :
        count = 0
        for n in list(set(dic[m])):
            if n in banned:
                count += 1
        answer.append(count)
        
    return answer