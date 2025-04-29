def max_prefix_free_subset(words):
    words = list(set(words))  # 중복 제거
    words.sort()  # 사전 순 정렬

    answer = 0
    for i in range(len(words)):
        is_prefix = False
        for j in range(i + 1, len(words)):
            if words[j].startswith(words[i]):
                is_prefix = True
                break
        if not is_prefix:
            answer += 1
    return answer

# 입력 처리
n = int(input())
words = [input().strip() for _ in range(n)]

print(max_prefix_free_subset(words))