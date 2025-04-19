# 입력 받기
a_len, b_len = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

# 대칭 차집합
sym_diff = a_set ^ b_set  # 또는 (a_set - b_set) | (b_set - a_set)

# 결과 출력
print(len(sym_diff))
