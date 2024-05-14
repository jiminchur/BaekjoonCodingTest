def solution(tickets):
    graph = dict()
    for start, end in tickets:
        if start not in graph:
            graph[start] = [end]
        else :
            graph[start].append(end)
    for key in graph.keys():
        graph[key].sort(reverse = True)
    
    stack = ["ICN"]
    answer = []
    
    while stack :
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            answer.append(stack.pop())
        else :
            stack.append(graph[top].pop())
    
    return answer[::-1]