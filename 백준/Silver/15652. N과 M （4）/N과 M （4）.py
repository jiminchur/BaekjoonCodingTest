N, M = map(int, input().split())
result = []

def dfs(start, depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N + 1):  # start부터 시작 → 비내림차순 보장
        result.append(i)
        dfs(i, depth + 1)  # 다음 탐색도 i부터 시작 (중복 허용)
        result.pop()

dfs(1, 0)