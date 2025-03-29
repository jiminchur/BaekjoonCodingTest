def solve():
    import sys
    input = sys.stdin.readline

    # 입력 받기
    N = int(input().strip())
    prices = list(map(int, input().split()))
    M = int(input().strip())

    # 0이 아닌 숫자 중 가장 낮은 가격과 해당 숫자 구하기 (첫 자리에 사용)
    min_nonzero = float('inf')
    first_digit = -1
    for i in range(1, N):
        if prices[i] < min_nonzero:
            min_nonzero = prices[i]
            first_digit = i

    # 만약 M으로 첫 자리에 쓸 수 있는 숫자를 살 수 없다면
    if M < min_nonzero:
        print("0")
        return

    # 전체 숫자 중 가장 낮은 가격과 해당 숫자 구하기 (나머지 자리에 사용)
    min_cost = min(prices)
    overall_digit = prices.index(min_cost)

    # 최대 자릿수 계산 (첫 자리에는 0이 아닌 최저가 숫자, 나머지는 전체 최저가 숫자 사용)
    max_digits = (M - min_nonzero) // min_cost + 1

    # 초기 방 번호 구성
    answer = [None] * max_digits
    answer[0] = first_digit
    for i in range(1, max_digits):
        answer[i] = overall_digit

    # 초기 구매 비용 및 남은 예산 계산
    money_spent = min_nonzero + (max_digits - 1) * min_cost
    remaining = M - money_spent

    # 왼쪽부터 차례로 업그레이드 시도 (더 큰 숫자로 교체)
    for i in range(max_digits):
        # 각 자리의 기준 비용 (첫 자리와 나머지 자리가 다를 수 있음)
        base_cost = prices[answer[i]]
        # 가능한 숫자 후보: N-1부터 0까지 (단, 첫 자리일 경우 0은 건너뜀)
        for d in range(N - 1, -1, -1):
            if i == 0 and d == 0 and max_digits > 1:
                continue
            # 만약 더 큰 숫자로 교체가 가능하면 (추가 비용이 남은 예산 이하인지 확인)
            cost_diff = prices[d] - base_cost
            if cost_diff <= remaining and d > answer[i]:
                answer[i] = d
                remaining -= cost_diff
                break  # 해당 자리에서는 한번 교체한 후 다음 자리로

    # 최종 방 번호 출력
    print("".join(map(str, answer)))


if __name__ == '__main__':
    solve()