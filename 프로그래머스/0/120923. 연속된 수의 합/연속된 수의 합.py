def solution(num, total):
    answer = []
    n = (total-sum(list(range(num))))//num
    for i in range(num):
        answer.append(n+i)
    return answer