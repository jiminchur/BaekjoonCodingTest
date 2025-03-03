def solution(n):
    answer = 0
    k = 1
    while True :
        number = 0
        if k == n+1:
            break
        for i in range(k,n+1):
            number += i
            if number == n:
                answer += 1
            if number >= n + 1:
                break
        k += 1
    return answer