from itertools import combinations

# 소수 구하는 함수
def find_decimal(lst):
    decimal_lst = []
    for i in lst:
        count = 0
        if int(i) != 0 and int(i) != 1:
            for k in range(2,int(i)):
                if int(i) % int(k) == 0:
                    count += 1
                    break
            if count == 0:
                decimal_lst.append(i)
    return decimal_lst

from itertools import permutations

# 모든 숫자 조합 구하는 함수
def all_possible_numbers(nums):
    # 가능한 모든 조합을 저장할 집합
    all_combinations = set()

    # 모든 가능한 길이에 대해 순열을 생성
    for r in range(1, len(nums) + 1):
        for combo in permutations(nums, r):
            # 각 순열로부터 숫자를 생성
            number = int("".join(map(str, combo)))
            # 생성된 숫자를 집합에 추가
            all_combinations.add(number)
    
    # 정렬된 리스트로 반환
    return sorted(list(all_combinations))


def solution(numbers):
    answer = 0
    str_nums = list(numbers)
    
    all_comb_lst = all_possible_numbers(str_nums)
    print(all_comb_lst)
    answer_ = find_decimal(all_comb_lst)
    print(answer_)
    answer = len(answer_)

    return answer