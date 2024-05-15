def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1 
    
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  
                dp[i][j] = 0
            else:
                if i > 1:
                    dp[i][j] += dp[i-1][j] % MOD
                if j > 1:
                    dp[i][j] += dp[i][j-1] % MOD
    
    return dp[n][m] % MOD
