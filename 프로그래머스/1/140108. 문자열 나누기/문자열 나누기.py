def solution(s):
    lst = list(s)
    count = 0
    answer = 0
    for i in lst:
        if count == 0 or check == i:
            check = i
            count += 1
        else :
            count -= 1
            if count == 0:
                answer += 1
    if count > 0:
        answer += 1
    return answer