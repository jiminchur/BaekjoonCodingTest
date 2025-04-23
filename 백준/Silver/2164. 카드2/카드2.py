import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
dq = deque(range(1, n+1))

while len(dq) > 1:
    dq.popleft()        # 맨 앞 버리고
    dq.append(dq.popleft())  # 다음 카드를 맨 뒤로

print(dq[0])