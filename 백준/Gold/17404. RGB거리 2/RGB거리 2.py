import sys
input = sys.stdin.readline
INF = float('inf')
N = int(input().strip())
costs = [list(map(int, input().split())) for _ in range(N)]
answer = INF

# 1번 집의 색을 빨강(0), 초록(1), 파랑(2) 중 하나로 고정하고 각각의 경우에 대해 DP를 진행한다.
for first_color in range(3):
    # dp[i][c] : i번째 집까지 칠할 때, i번째 집을 색 c로 칠한 최소 비용
    dp = [[INF] * 3 for _ in range(N)]
    # 첫 번째 집은 고정한 색만 실제 비용을 넣는다.
    dp[0][first_color] = costs[0][first_color]

    # 집 2부터 N번 집까지 순서대로 처리
    for i in range(1, N):
        # i번째 집을 빨강(0)으로 칠할 때
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        # i번째 집을 초록(1)으로 칠할 때
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        # i번째 집을 파랑(2)로 칠할 때
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    # 마지막 집(N번 집)에서는 첫 집의 색과 다르게 칠해야 한다.
    for color in range(3):
        if color == first_color:
            continue
        answer = min(answer, dp[N-1][color])
    
print(answer)