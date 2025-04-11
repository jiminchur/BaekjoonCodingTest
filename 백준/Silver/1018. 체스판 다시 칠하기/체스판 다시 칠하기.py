# 입력은 sys.stdin.readline을 사용할 수 있지만 여기서는 input()을 가정합니다.
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

def count_recolors(x, y):
    # 두 가지 패턴에 대해 재도색해야 하는 개수 계산
    count1, count2 = 0, 0
    for i in range(8):
        for j in range(8):
            # 현재 보드의 문자
            current = board[x + i][y + j]
            # (i+j)의 짝수 여부에 따라 기대 색 결정:
            # 패턴1: 맨 왼쪽이 'W'라면, (i+j)%2==0 → 'W', 아니면 'B'
            expected1 = 'W' if (i+j) % 2 == 0 else 'B'
            # 패턴2: 맨 왼쪽이 'B'라면, (i+j)%2==0 → 'B', 아니면 'W'
            expected2 = 'B' if (i+j) % 2 == 0 else 'W'
            if current != expected1:
                count1 += 1
            if current != expected2:
                count2 += 1
    # 두 패턴 중 더 적은 재도색 수 반환
    return min(count1, count2)

min_recolors = float('inf')
# 가능한 모든 8x8 보드 위치를 탐색
for i in range(N - 7):
    for j in range(M - 7):
        min_recolors = min(min_recolors, count_recolors(i, j))

print(min_recolors)