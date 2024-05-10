# def solution(citations):
#     answer = 0
#     citations.sort()
#     for check in range(citations.__len__()):
#         if citations[check] == len(citations[check:]) and citations[check] >= len(citations[:check+1]):
#             answer = citations[check]
#     return answer

def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    h_index = 0  # 초기 H-Index 값은 0으로 설정
    for i, citation in enumerate(citations):
        if i + 1 <= citation:
            h_index = i + 1  # 논문의 인덱스(1부터 시작하는 것으로 가정)가 인용 횟수보다 작거나 같으면 H-Index를 업데이트
        else:
            break  # 논문의 인덱스가 인용 횟수보다 크면 반복을 멈춤
    return h_index
