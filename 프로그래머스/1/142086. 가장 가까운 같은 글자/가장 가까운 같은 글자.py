def solution(s):
    answer = []
    s_lst = list(s)
    s_dic = {}
    for i in range(len(s_lst)) :
        try :
            answer.append(i - s_dic[s_lst[i]])
            s_dic[s_lst[i]] = i
        except :
            s_dic[s_lst[i]] = i
            answer.append(-1)
    return answer