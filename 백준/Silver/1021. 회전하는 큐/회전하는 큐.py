from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))
dq = deque(range(1, n + 1))

operations = 0

for target in targets:
    idx = dq.index(target)
    if idx <= len(dq) // 2:
        # 왼쪽으로 회전
        dq.rotate(-idx)
        operations += idx
    else:
        # 오른쪽으로 회전
        dq.rotate(len(dq) - idx)
        operations += len(dq) - idx
    dq.popleft()  # 원하는 값 제거

print(operations)