N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]

# 트리 구성
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 루트로부터 각 노드까지 거리 저장
dist = [0] * (N+1)
visited = [False] * (N+1)

def dfs(node, acc):
    visited[node] = True
    dist[node] = acc
    for neighbor, weight in tree[node]:
        if not visited[neighbor]:
            dfs(neighbor, acc + weight)

dfs(1, 0)  # 루트를 1번 노드로 설정

# 쿼리 처리
def get_distance(a, b):
    visited = [False] * (N+1)
    answer = [0]
    
    def dfs2(cur, target, acc):
        if cur == target:
            answer[0] = acc
            return
        visited[cur] = True
        for nxt, w in tree[cur]:
            if not visited[nxt]:
                dfs2(nxt, target, acc + w)

    dfs2(a, b, 0)
    return answer[0]

for _ in range(M):
    a, b = map(int, input().split())
    print(get_distance(a, b))