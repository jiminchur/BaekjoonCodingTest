# def solution(A, B):
#     sort_a, sort_b = sorted(A), sorted(B)
#     answer = 0
#     index_a = 0
    
#     for b in sort_b:
#         if index_a < len(sort_a) and sort_a[index_a] < b:
#             answer += 1
#             index_a += 1
#         elif index_a < len(sort_a) and sort_a[index_a] == b:
#             index_a += 1
            
#     return answer
def solution(A, B):
    # A와 B를 정렬합니다.
    A.sort()
    B.sort()
    
    # 포인터 초기화
    points = 0
    j = 0  # B팀의 포인터
    
    # A팀의 각 숫자에 대해 B팀의 적절한 숫자를 찾습니다.
    for a in A:
        # B팀의 현재 숫자가 A팀의 숫자보다 작거나 같은 경우, 다음 숫자를 찾습니다.
        while j < len(B) and B[j] <= a:
            j += 1
        # B팀의 현재 숫자가 A팀의 숫자보다 큰 경우, 점수를 얻습니다.
        if j < len(B):
            points += 1
            j += 1  # B팀의 포인터를 다음 숫자로 이동합니다.
    
    return points
