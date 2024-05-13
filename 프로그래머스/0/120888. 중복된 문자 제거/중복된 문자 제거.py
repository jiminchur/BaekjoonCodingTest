def solution(my_string):
    answer = ''
    str_lst = list(my_string)
    dic = {}
    lst = []
    for i in range(len(str_lst)) :
        try :
            dic[str_lst[i]]
            lst.append(i)
        except :
            dic[str_lst[i]] = 1
    lst.reverse()
    for k in lst :
        del str_lst[k]
    answer = "".join(str_lst)
    return answer