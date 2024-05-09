def solution(s):
    s_lst = list(s)
    check_lst = []
    if s_lst[0] == ")" or s_lst[-1] == "(" :
        return False
    else :
        for check in s_lst :
            check_lst.append(check)
            if check_lst.__len__() >=2 :
                if check_lst[-2] + check_lst[-1] == "()":
                    del check_lst[-2]
                    del check_lst[-1]
        if check_lst.__len__() > 0 :
            return False
        else :
            return True