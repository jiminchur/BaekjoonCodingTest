# from itertools import permutations

# def solution(numbers):
#     # 숫자들을 문자열로 변환
#     str_nums = list(map(str, numbers))
#     # 모든 순열 생성
#     all_combinations = permutations(str_nums)
#     # 각 순열을 문자열로 변환하고 최대값 찾기
#     answer = max(''.join(comb) for comb in all_combinations)

#     return answer

def solution(numbers):
    # 숫자를 문자열로 변환
    str_nums = map(str, numbers)
    # 문자열 비교를 위해 정렬
    # 두 문자열 a, b에 대해 a+b와 b+a를 비교하여 큰 순서로 정렬
    sorted_nums = sorted(str_nums, key=lambda x: x*3, reverse=True)
    # 정렬된 문자열을 합쳐서 결과 생성
    answer = ''.join(sorted_nums)
    
    return '0' if answer[0] == '0' else answer

