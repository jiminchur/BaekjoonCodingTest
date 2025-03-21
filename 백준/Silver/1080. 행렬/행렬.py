import sys
from itertools import product

def in_range(N, M):
    n_lst = range(N - 2)
    m_lst = range(M - 2)
    return list(product(n_lst, m_lst))

def flip(A, x, y):
    # 주어진 위치 (x, y)를 기준으로 3x3 행렬을 뒤집기
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]

def procession(A, B, N, M):
    cnt = 0
    for x, y in in_range(N, M):
        if A[x][y] != B[x][y]:
            flip(A, x, y)
            cnt += 1

    # 최종적으로 A와 B가 같은지 확인
    if A == B:
        return cnt
    else:
        return -1

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 크기가 3 미만이면 뒤집기 불가능한데, 두 행렬이 같다면 0, 아니라면 -1
if N < 3 or M < 3:
    print(0 if A == B else -1)
else:
    print(procession(A, B, N, M))