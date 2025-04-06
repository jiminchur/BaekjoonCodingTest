# 입력 받기
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

max_area = 1  # 최소 정사각형 면적은 1 (한 칸)

# 모든 가능한 시작 좌표와 정사각형 크기 L에 대해 검사
for i in range(N):
    for j in range(M):
        # 최대 정사각형의 한 변 길이 (L+1)가 min(N, M) 이하이어야 함
        for L in range(1, min(N, M)):
            # (i, j)에서 한 변의 길이가 L인 정사각형이 격자 내에 존재하는지 확인
            if i + L < N and j + L < M:
                # 네 꼭짓점의 숫자가 모두 같은지 확인
                if grid[i][j] == grid[i][j + L] == grid[i + L][j] == grid[i + L][j + L]:
                    # 면적 = (L+1)²
                    max_area = max(max_area, (L + 1) ** 2)

print(max_area)