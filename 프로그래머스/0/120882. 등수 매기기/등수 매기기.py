def solution(score):
    answer = []
    mean_lst = []
    rank_dic = dict()
    
    for i in score :
        mean_lst.append(sum(i)/len(i))
        
    mean_lst_ = mean_lst.copy()
    mean_lst_.sort(reverse=True)
    
    for k,mean in enumerate(mean_lst_) :
        if mean not in rank_dic :
            rank_dic[mean] = [k + 1]
        else:
            rank_dic[mean].append([k + 1])
    for i in mean_lst :
        answer.append(rank_dic[i][0])
    return answer