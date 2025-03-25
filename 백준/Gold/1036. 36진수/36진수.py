from collections import defaultdict

# 문자 -> 숫자
def to_num(c):
    return int(c) if c.isdigit() else ord(c) - ord('A') + 10

# 숫자 -> 문자
def to_char(n):
    return str(n) if n < 10 else chr(ord('A') + n - 10)

# 10진수 -> 36진수
def to_36_base(n):
    if n == 0:
        return '0'
    res = ''
    while n:
        n, r = divmod(n, 36)
        res = to_char(r) + res
    return res

# 메인 로직
N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())

profit = defaultdict(int)

# 각 문자별로 Z로 바꿀 때 이득을 계산
for num in nums:
    for i, c in enumerate(num[::-1]):
        profit[c] += (35 - to_num(c)) * (36 ** i)

# 가장 이득이 큰 문자 K개 선택
change_chars = {c for c, _ in sorted(profit.items(), key=lambda x: -x[1])[:K]}

# K개 문자를 Z로 변경 후 합 계산
total_sum = sum(int(''.join('Z' if c in change_chars else c for c in num), 36) for num in nums)

# 결과 출력
print(to_36_base(total_sum))
