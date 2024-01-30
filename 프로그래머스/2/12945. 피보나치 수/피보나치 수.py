def solution(n):
    answer = 0
    a_lst = [0,1]
    
    for i in range(2,n+1):
        c = a_lst[-2] + a_lst[-1]
        a_lst.append(c)
    answer_ = a_lst[-1]
    answer = answer_ % 1234567
    return answer