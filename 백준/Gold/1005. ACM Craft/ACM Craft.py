from collections import deque
import sys
input = sys.stdin.readline

def solve():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        D = [0] + list(map(int, input().split()))
        graph = [[] for _ in range(N+1)]
        indegree = [0] * (N+1)

        for _ in range(K):
            X, Y = map(int, input().split())
            graph[X].append(Y)
            indegree[Y] += 1

        W = int(input())

        queue = deque()
        dp = [0] * (N+1)

        # 진입 차수가 0인 건물을 큐에 넣음
        for i in range(1, N+1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = D[i]

        # 위상 정렬 수행
        while queue:
            curr = queue.popleft()

            for next_node in graph[curr]:
                indegree[next_node] -= 1
                # 선행 건물 중 가장 늦게 완성된 시간으로 업데이트
                dp[next_node] = max(dp[next_node], dp[curr] + D[next_node])

                if indegree[next_node] == 0:
                    queue.append(next_node)

        print(dp[W])

if __name__ == "__main__":
    solve()