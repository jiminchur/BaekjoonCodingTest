def solution(clothes):
    from collections import defaultdict
    
    clothe_dict = defaultdict(int)
    
    # 카테고리별 의상 개수 세기
    for _, category in clothes:
        clothe_dict[category] += 1

    # 각 카테고리별 (의상 개수 + 1) 곱하기
    combinations = 1
    for count in clothe_dict.values():
        combinations *= (count + 1)  # 안 입는 경우 포함

    return combinations - 1  # 모두 안 입는 경우 제외