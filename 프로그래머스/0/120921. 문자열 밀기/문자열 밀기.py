def solution(A, B):
    # A와 B가 이미 같은 경우, 밀어야 하는 횟수는 0입니다.
    if A == B:
        return 0
    
    # A의 길이만큼 반복합니다. 이는 문자열을 한 바퀴 돌리는 것과 같습니다.
    for i in range(len(A)):
        # A를 오른쪽으로 1칸 밀어서 새로운 문자열을 생성합니다.
        A = A[-1] + A[:-1]  # 마지막 문자를 맨 앞으로, 나머지 문자열을 뒤로 이동합니다.
        
        # 밀어서 생성된 새로운 A가 B와 같다면, 현재의 반복 횟수(i+1)을 반환합니다.
        if A == B:
            return i + 1
    
    # 모든 경우를 시도했음에도 B를 만들 수 없는 경우, -1을 반환합니다.
    return -1
