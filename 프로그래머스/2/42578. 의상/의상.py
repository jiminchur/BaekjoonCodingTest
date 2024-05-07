# from itertools import combinations

# def solution(clothes):
#     category = []
#     answer = 0
#     for kinds in clothes :
#         category.append(kinds[1])
    
#     for i in range(1,len(category) + 1):
#         for comb in combinations(category, i):
#             true_count = len(comb)
#             dupli_count = len(list(set(comb)))
#             if true_count == dupli_count:
#                 answer += 1
#     return answer
def solution(clothes):
    from collections import defaultdict
    
    # 의상 종류별로 의상의 수를 저장할 딕셔너리
    clothes_dict = defaultdict(int)
    
    # 의상 종류별로 의상의 수를 센다
    for _, clothe_type in clothes:
        clothes_dict[clothe_type] += 1
    
    # 모든 조합의 수를 계산한다 (각 종류별 의상 수 + 1 의 곱)
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)
    
    # 모든 종류에서 아무것도 선택하지 않는 경우 1가지를 빼서 결과를 구한다
    return answer - 1