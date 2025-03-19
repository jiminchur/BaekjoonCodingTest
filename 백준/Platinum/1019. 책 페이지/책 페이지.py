def count_digits(N):
    counts = [0] * 10
    point = 1
    start = 1
    end = N

    while start <= end:
        # start의 일의 자리를 0으로 맞추기
        while start % 10 != 0 and start <= end:
            count_each_digit(start, counts, point)
            start += 1

        # end의 일의 자리를 9로 맞추기
        while end % 10 != 9 and start <= end:
            count_each_digit(end, counts, point)
            end -= 1

        if start > end:
            break

        # 0부터 9까지 각 숫자가 현재 자리수에서 등장하는 횟수 누적
        start_div_10 = start // 10
        end_div_10 = end // 10
        count_range = end_div_10 - start_div_10 + 1
        for i in range(10):
            counts[i] += count_range * point

        # 다음 자리수로 이동
        start //= 10
        end //= 10
        point *= 10

    return counts

def count_each_digit(number, counts, point):
    while number > 0:
        digit = number % 10
        counts[digit] += point
        number //= 10

# 예시 사용
N = int(input())
result = count_digits(N)
print(" ".join(map(str, result)))