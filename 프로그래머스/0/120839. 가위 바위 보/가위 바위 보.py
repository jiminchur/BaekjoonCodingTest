def solution(rsp):
    rsp_lst = list(rsp)
    win_dic = {"0":"5","5":"2","2":"0"}
    answer = ''
    for pick in rsp_lst:
        answer += win_dic[pick]
    return answer