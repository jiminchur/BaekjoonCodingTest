from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == n-1 and y == m-1:
            return cnt
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, cnt + 1))
    
    return -1