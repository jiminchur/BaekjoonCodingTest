def solution(emergency):
    answer = []
    dic = dict()
    emergency_ = emergency.copy()
    emergency_.sort(reverse=True)
    for i , n in enumerate(emergency_):
        dic[n] = i+1
    
    for rank in emergency:
        answer.append(dic[rank])
    return answer