L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

if n in S:
    print(0)
else:
    left = 0
    right = 1001

    for s in S:
        if s < n:
            left = s
        elif s > n and right > s:
            right = s

    result = (n - left) * (right - n) - 1
    print(result)