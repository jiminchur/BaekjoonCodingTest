def solution(n):
    answer = 0
    i = 0
    while True:
        i += 2
        if i > n :
            break
        answer += i
        
    return answer