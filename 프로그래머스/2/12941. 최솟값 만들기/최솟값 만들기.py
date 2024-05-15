def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(A.__len__()):
        c = A[i]*B[i]
        answer += c
    return answer