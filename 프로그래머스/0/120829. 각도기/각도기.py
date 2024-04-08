def solution(angle):
    if angle % 90 == 0:
        answer = angle // 90 * 2 
    elif angle < 90 :
        answer = 1
    else :
        answer = 3
    return answer