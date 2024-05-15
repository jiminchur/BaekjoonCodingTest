def solution(d, budget):
    answer = 0
    d.sort()
    for i,n in enumerate(d):
        if n > budget :
            return i
        else :
            budget -= n
    answer = len(d)
    return answer