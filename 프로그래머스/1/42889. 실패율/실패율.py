def solution(N, stages):
    answer = []
    all_user = len(stages)
    stage_lst = [stages.count(i) for i in range(1,N+1)]
    dic = dict()
    for i,n in enumerate(stage_lst):
        if all_user > 0:
            fail = n/all_user
        else :
            fail = 0
        if fail not in dic:
            dic[fail] = [i+1]
        else :
            dic[fail].append(i+1)
        all_user -= n
    dic_lst = list(dic.keys())
    dic_lst.sort(reverse=True)
    
    for k in dic_lst :
        answer += dic[k]
    return answer