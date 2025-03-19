import re

# 패턴 설정
pattern = re.compile('(100+1+|01)+')

# 입력 받기
T = int(input())
for _ in range(T):
    signal = input().strip()
    # 패턴 일치 확인
    if pattern.fullmatch(signal):
        print("YES")
    else:
        print("NO")