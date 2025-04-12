import sys

def solve():
    input = sys.stdin.readline
    # N: 지름길 개수, D: 고속도로 길이
    N, D = map(int, input().split())
    shortcuts = []
    
    for _ in range(N):
        s, e, d = map(int, input().split())
        # 편익이 있는 지름길만 고려: 고속도로 이동보다 짧아야 하고, 도착 지점이 D 이하인 경우
        if e <= D and d < (e - s):
            shortcuts.append((s, e, d))
    
    # dp[i]: 0부터 i까지 가는 최소 거리
    dp = [i for i in range(D + 1)]
    
    # 0부터 D까지 각 킬로미터마다 최소거리를 갱신
    for i in range(D + 1):
        # 고속도로를 1km 이동하는 경우
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        # 시작점이 i인 지름길들을 확인
        for s, e, d in shortcuts:
            if s == i:
                if e <= D:
                    dp[e] = min(dp[e], dp[i] + d)
    
    print(dp[D])

if __name__ == '__main__':
    solve()