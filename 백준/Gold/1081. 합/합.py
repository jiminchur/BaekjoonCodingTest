def sum_digits_upto(n):
    if n < 10:
        return n * (n + 1) // 2

    # n의 자릿수를 구하고, 가장 높은 자리의 값을 분리한다.
    s = str(n)
    d = len(s) - 1       # 남은 자리수(최상위 자리 제외)
    p = 10 ** d          # 10^d, 예를 들어 1234이면 p는 1000
    msd = n // p         # 가장 높은 자리의 숫자
    return (msd * sum_digits_upto(p - 1) +
            (msd * (msd - 1) // 2) * p +
            msd * (n % p + 1) +
            sum_digits_upto(n % p))


import sys
input_line = sys.stdin.readline().strip()
if not input_line:
    input_line = sys.stdin.read().strip()
L, U = map(int, input_line.split())

    
if L > 0:
    result = sum_digits_upto(U) - sum_digits_upto(L - 1)
else:
    result = sum_digits_upto(U)

print(result)