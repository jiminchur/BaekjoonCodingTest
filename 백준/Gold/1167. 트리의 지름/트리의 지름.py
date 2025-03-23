import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 정점의 개수 읽기
V = int(input().strip())
graph = [[] for _ in range(V + 1)]

# 인접 리스트 구성 (각 줄의 마지막 -1은 입력 종료를 의미)
for _ in range(V):
    data = list(map(int, input().split()))
    u = data[0]
    idx = 1
    while data[idx] != -1:
        v = data[idx]
        d = data[idx + 1]
        graph[u].append((v, d))
        idx += 2

# 전역 변수로 최대 거리와 그 때의 정점을 저장
max_distance = 0
farthest_node = 0

def dfs(node, dist, visited):
    global max_distance, farthest_node
    # 현재까지의 거리가 최대라면 갱신
    if dist > max_distance:
        max_distance = dist
        farthest_node = node
    # 인접 정점 탐색
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, dist + weight, visited)

# 1. 임의의 정점(여기서는 1번)에서 DFS를 시작하여 가장 먼 정점을 찾는다.
visited = [False] * (V + 1)
visited[1] = True
dfs(1, 0, visited)

# 첫 번째 DFS 결과: farthest_node에는 1번에서 가장 멀리 떨어진 정점이 저장됨.
# max_distance는 이때의 거리를 의미하지만, 트리의 지름을 구하기 위해 두 번째 DFS를 진행한다.

# 2. 첫 번째 DFS에서 찾은 farthest_node에서 다시 DFS를 시작한다.
start = farthest_node
visited = [False] * (V + 1)
visited[start] = True
max_distance = 0  # 최대 거리 초기화
dfs(start, 0, visited)

# 두 번째 DFS에서 구한 max_distance가 트리의 지름이다.
print(max_distance)