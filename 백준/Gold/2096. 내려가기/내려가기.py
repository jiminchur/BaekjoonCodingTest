import sys

N = int(sys.stdin.readline())

max_dp = list(map(int, sys.stdin.readline().split()))
min_dp = max_dp

for _ in range(1, N):
    current_row = list(map(int, sys.stdin.readline().split()))
    
    new_max_dp = [0] * 3
    new_min_dp = [0] * 3
    
    new_max_dp[0] = max(max_dp[0], max_dp[1]) + current_row[0]
    new_max_dp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + current_row[1]
    new_max_dp[2] = max(max_dp[1], max_dp[2]) + current_row[2]
    
    new_min_dp[0] = min(min_dp[0], min_dp[1]) + current_row[0]
    new_min_dp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + current_row[1]
    new_min_dp[2] = min(min_dp[1], min_dp[2]) + current_row[2]
    
    max_dp = new_max_dp
    min_dp = new_min_dp

print(max(max_dp), min(min_dp))