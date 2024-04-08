def solution(array):
    answer = 0
    lst = sorted(array)
    median = lst.__len__()//2
    answer = lst[median]
    return answer