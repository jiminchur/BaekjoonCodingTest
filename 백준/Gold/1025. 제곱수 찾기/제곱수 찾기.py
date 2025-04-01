import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
ans = -1

for i in range(N):
    for j in range(M):
        for dr in range(-N + 1, N):
            for dc in range(-M + 1, M):
                # dr, dc가 모두 0인 경우 -> 한 칸만 선택하는 경우
                if dr == 0 and dc == 0:
                    num = int(grid[i][j])
                    if math.isqrt(num) ** 2 == num:
                        ans = max(ans, num)
                    continue

                x, y = i, j
                num_str = ""
                while 0 <= x < N and 0 <= y < M:
                    num_str += grid[x][y]
                    num = int(num_str)
                    if math.isqrt(num) ** 2 == num:
                        ans = max(ans, num)
                    x += dr
                    y += dc

print(ans)