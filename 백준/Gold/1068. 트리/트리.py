def solve():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    parent_list = list(map(int, input().split()))
    remove_node = int(input().strip())

    # 자식 리스트 생성
    children = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        p = parent_list[i]
        if p == -1:
            root = i
        else:
            children[p].append(i)

    # 만약 삭제할 노드가 루트라면 트리가 모두 삭제되므로 0 출력
    if remove_node == root:
        print(0)
        return

    # 삭제할 노드와 그 자손들을 DFS로 탐색하여 제거 표시
    removed = [False] * n

    def dfs_delete(node):
        removed[node] = True
        for child in children[node]:
            if not removed[child]:
                dfs_delete(child)

    dfs_delete(remove_node)

    # 남은 트리에서 리프 노드(자식이 없거나, 모두 삭제된 경우) 개수 세기
    leaf_count = 0
    for i in range(n):
        if removed[i]:
            continue
        is_leaf = True
        for child in children[i]:
            if not removed[child]:
                is_leaf = False
                break
        if is_leaf:
            leaf_count += 1

    print(leaf_count)

if __name__ == "__main__":
    solve()