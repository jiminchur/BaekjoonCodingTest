def solve():
    import sys
    input = sys.stdin.readline
    
    N = int(input().strip())
    seq = list(map(int, input().split()))
    
    # N = 1인 경우
    if N == 1:
        print("A")
        return
    
    # N = 2인 경우
    if N == 2:
        # 두 숫자가 같으면 다음 숫자도 같다.
        if seq[0] == seq[1]:
            print(seq[0])
        else:
            print("A")
        return
    
    # N >= 3 인 경우
    # 만약 첫 두 숫자가 같은 경우, 모든 숫자가 같아야 함.
    if seq[0] == seq[1]:
        same = True
        for num in seq:
            if num != seq[0]:
                same = False
                break
        if same:
            print(seq[0])
        else:
            print("B")
        return
    
    # seq[0] != seq[1] 인 경우: a, b 구하기
    diff = seq[1] - seq[0]
    # 분모가 0이 아니므로 a 계산 가능
    # a가 정수가 되는지 확인 (소수점 판별)
    if (seq[2] - seq[1]) % diff != 0:
        print("B")
        return
    a = (seq[2] - seq[1]) // diff
    b = seq[1] - a * seq[0]
    
    # 전체 수열이 규칙에 부합하는지 확인
    valid = True
    for i in range(1, N):
        if seq[i] != seq[i-1] * a + b:
            valid = False
            break
    
    if not valid:
        print("B")
    else:
        # 다음 수 계산
        next_num = seq[-1] * a + b
        print(next_num)

# 아래 코드는 테스트용입니다.
if __name__ == '__main__':
    solve()