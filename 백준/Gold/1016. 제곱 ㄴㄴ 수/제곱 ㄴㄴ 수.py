def count_square_free_numbers(min_val, max_val):
    range_size = max_val - min_val + 1
    is_square_free = [True] * range_size

    max_check = int(max_val**0.5) + 1

    for i in range(2, max_check):
        square = i * i
        start = ((min_val + square - 1) // square) * square

        for j in range(start, max_val + 1, square):
            is_square_free[j - min_val] = False

    return sum(is_square_free)

# 입력 받기
min_val, max_val = map(int, input().split())

# 제곱ㄴㄴ수 개수 계산
result = count_square_free_numbers(min_val, max_val)

# 결과 출력
print(result)