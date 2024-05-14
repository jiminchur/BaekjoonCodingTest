def dfs(computers,visited,start):
    visited[start] = True
    for k in range(len(computers)):
        if computers[start][k] == 1 and not visited[k]:
            dfs(computers,visited,k)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers,visited,i)
            answer += 1
    return answer