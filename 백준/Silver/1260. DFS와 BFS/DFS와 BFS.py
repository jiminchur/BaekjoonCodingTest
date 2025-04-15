from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS와 BFS 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)