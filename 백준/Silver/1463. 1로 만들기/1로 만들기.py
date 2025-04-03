def make_one(N):
    dp = [0] * (N + 1)
    
    for i in range(2, N + 1):
        # 기본 연산: 1을 뺀 경우
        dp[i] = dp[i - 1] + 1
        
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[N]

# 입력
N = int(input())
print(make_one(N))