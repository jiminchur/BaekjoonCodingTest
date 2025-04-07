# 입력: 첫 줄에 노드의 개수, 그 후 각 노드 정보 (루트, 왼쪽 자식, 오른쪽 자식)
n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return node + preorder(left) + preorder(right)

# 중위 순회: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return inorder(left) + node + inorder(right)

# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return postorder(left) + postorder(right) + node

# A가 루트이므로 'A'부터 순회
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))