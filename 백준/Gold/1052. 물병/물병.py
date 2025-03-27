def min_bottles_to_buy(N, K):
    count = 0
    while bin(N).count('1') > K:
        N += 1
        count += 1
    return count

# 입력
N, K = map(int, input().split())
print(min_bottles_to_buy(N, K))