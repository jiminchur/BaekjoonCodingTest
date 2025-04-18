def josephus(N, K):
    people = list(range(1, N + 1))
    result = []
    index = 0

    while people:
        index = (index + K - 1) % len(people)  # K번째 사람의 인덱스 계산
        result.append(people.pop(index))       # 제거 후 결과에 추가

    return result

# 입력
N, K = map(int, input().split())
sequence = josephus(N, K)

# 출력 형식 맞춰서 출력
print("<" + ", ".join(map(str, sequence)) + ">")