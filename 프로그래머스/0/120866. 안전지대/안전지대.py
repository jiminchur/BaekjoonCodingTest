dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def solution(board):
    n = len(board)
    safe_area = [[1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe_area[i][j] = 0
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        safe_area[nx][ny] = 0

    return sum(sum(row) for row in safe_area)
