import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0] * M for _ in range(N)]

# 시작 지점 초기화
dp[0][0] = maze[0][0]

# DP 테이블 채우기
for i in range(N):
    for j in range(M):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + maze[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + maze[i][j])
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + maze[i][j])

# 결과 출력
print(dp[N-1][M-1])
