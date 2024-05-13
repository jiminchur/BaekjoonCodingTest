def solution(my_str, n):
    answer = []
    result_str = ''
    count = 0
    str_lst = list(my_str)
    for my in str_lst:
        if count == n :
            answer.append(result_str)
            result_str = my
            count = 1
        else :
            count += 1
            result_str += my
    if len(result_str) > 0 :
        answer.append(result_str)
    return answer