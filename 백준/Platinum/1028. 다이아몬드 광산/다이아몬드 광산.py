def largest_diamond_size(R, C, mine):
    # 4개의 방향으로 연속된 1의 개수를 저장할 배열 초기화
    ld = [[0] * (C + 2) for _ in range(R + 2)]  # ↙ 방향
    rd = [[0] * (C + 2) for _ in range(R + 2)]  # ↘ 방향
    lu = [[0] * (C + 2) for _ in range(R + 2)]  # ↖ 방향
    ru = [[0] * (C + 2) for _ in range(R + 2)]  # ↗ 방향

    # 광산 배열을 1로 패딩하여 인덱스 에러 방지
    padded_mine = [[0] * (C + 2)] + [[0] + row + [0] for row in mine] + [[0] * (C + 2)]

    # ↙ 및 ↘ 방향의 연속된 1의 개수 계산
    for i in range(R, 0, -1):
        for j in range(1, C + 1):
            if padded_mine[i][j] == 1:
                ld[i][j] = ld[i + 1][j - 1] + 1
                rd[i][j] = rd[i + 1][j + 1] + 1

    # ↖ 및 ↗ 방향의 연속된 1의 개수 계산
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if padded_mine[i][j] == 1:
                lu[i][j] = lu[i - 1][j - 1] + 1
                ru[i][j] = ru[i - 1][j + 1] + 1

    max_size = 0

    # 각 위치에서 다이아몬드의 최대 크기 계산
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            # ↙ 및 ↘ 방향의 최소값이 해당 위치에서의 최대 다이아몬드 크기 후보
            possible_size = min(ld[i][j], rd[i][j])
            while possible_size > max_size:
                # 아래쪽 꼭짓점의 좌표
                bottom_i = i + 2 * (possible_size - 1)
                if bottom_i > R:
                    possible_size -= 1
                    continue
                # 아래쪽 꼭짓점에서 ↖ 및 ↗ 방향의 값이 현재 크기 이상인지 확인
                if lu[bottom_i][j] >= possible_size and ru[bottom_i][j] >= possible_size:
                    max_size = possible_size
                possible_size -= 1

    return max_size

# 입력 처리
R, C = map(int, input().split())
mine = [list(map(int, list(input().strip()))) for _ in range(R)]

# 결과 출력
print(largest_diamond_size(R, C, mine))