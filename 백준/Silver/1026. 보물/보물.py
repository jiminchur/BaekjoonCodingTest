N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()              # A는 오름차순
B_sorted = sorted(B, reverse=True)  # B는 내림차순 (원본 B는 유지)

S = sum(a * b for a, b in zip(A, B_sorted))
print(S)