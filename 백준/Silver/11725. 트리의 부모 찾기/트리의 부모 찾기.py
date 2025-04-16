import sys
sys.setrecursionlimit(10**6)

# 입력
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

# 간선 정보 저장
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS 함수 정의
def dfs(current):
    for neighbor in tree[current]:
        if parent[neighbor] == 0:
            parent[neighbor] = current
            dfs(neighbor)

# 루트를 1로 정하고 DFS 실행
dfs(1)

# 2번 노드부터 부모 출력
for i in range(2, n + 1):
    print(parent[i])