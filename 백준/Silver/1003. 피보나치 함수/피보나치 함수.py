# 피보나치 수에서 0과 1이 출력된 횟수를 미리 저장하는 DP테이블 생성
dp = [(1, 0), (0, 1)] + [(0, 0)] * 39

# DP 테이블 미리 계산
for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])