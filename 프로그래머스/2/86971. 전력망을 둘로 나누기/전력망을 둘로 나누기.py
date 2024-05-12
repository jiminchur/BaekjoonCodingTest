def solution(n, wires):
    from collections import defaultdict
    
    def dfs(graph, start, visited):
        # DFS 알고리즘을 사용하여 서브 트리의 노드 수를 계산
        count = 1
        visited[start] = True
        for neighbor in graph[start]:
            if not visited[neighbor]:
                count += dfs(graph, neighbor, visited)
        return count
    
    # 그래프 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = float('inf')  # 가능한 최대 차이로 초기화
    
    for v1, v2 in wires:
        # 각 간선을 제거하고 두 서브 트리의 노드 수 계산
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n + 1)
        count = dfs(graph, v1, visited)
        
        # 두 서브 트리의 노드 수 차이 계산
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)
        
        # 제거했던 간선 복구
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return min_diff
