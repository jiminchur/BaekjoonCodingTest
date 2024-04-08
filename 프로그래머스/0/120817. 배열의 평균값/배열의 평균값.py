def solution(numbers):
    all_sum = 0
    lst_len = numbers.__len__()
    
    for i in numbers:
        all_sum += i
    answer = round(all_sum / lst_len,1)
    
    test = str(answer).split(".")
    if int(test[1]) == 0 or int(test[1]) == 5:
        pass
    else :
        answer = int(str(answer).split('.')[0])
    return answer