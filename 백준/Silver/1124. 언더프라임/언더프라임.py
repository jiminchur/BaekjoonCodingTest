import sys
input = sys.stdin.read

def main():
    A, B = map(int, input().split())
    MAX = 100000

    # 1. 소수 여부 미리 계산 (에라토스테네스의 체)
    is_prime = [False, False] + [True] * (MAX - 1)
    for i in range(2, int(MAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, MAX + 1, i):
                is_prime[j] = False

    # 2. 각 수의 소인수 개수 계산
    prime_factor_count = [0] * (MAX + 1)
    for i in range(2, MAX + 1):
        if prime_factor_count[i] == 0:  # i는 소수
            for j in range(i, MAX + 1, i):
                k = j
                while k % i == 0:
                    prime_factor_count[j] += 1
                    k //= i

    # 3. 언더프라임 개수 세기
    count = 0
    for i in range(A, B + 1):
        if is_prime[prime_factor_count[i]]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()