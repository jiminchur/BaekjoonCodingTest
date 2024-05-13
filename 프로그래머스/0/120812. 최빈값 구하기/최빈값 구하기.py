def solution(array):
    answer = 0
    count = 0
    check_lst = list(set(array))
    for i in check_lst :
        if count > array.count(i):
            pass
        elif count < array.count(i):
            count = array.count(i)
            answer = i
        elif count == array.count(i):
            answer = -1
        
    return answer