def solution(chicken):
    answer = 0
    while True :
        if chicken // 10 == 0:
            break
        else :
            answer += chicken // 10
            chicken = chicken // 10 + chicken % 10
    return answer