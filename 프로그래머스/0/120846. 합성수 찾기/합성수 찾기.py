def solution(n):
    non_answer = 1
    for i in range(2,n+1):
        a = 0
        for k in range(1,n+1):
            if i % k == 0:
                a += 1
        if a == 2:
            non_answer += 1
    answer = n - non_answer
    return answer