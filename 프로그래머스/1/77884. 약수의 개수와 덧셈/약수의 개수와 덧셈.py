def yak(k):
    count = 0
    for n in range(1,k+1):
        if k % n == 0:
            count += 1
    if count % 2 == 0:
        return 1
    else :
        return 0

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if yak(i) == 1 :
            answer += i
        else :
            answer -= i 
    return answer