def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # cards1과 cards2의 인덱스를 추적합니다.
    for word in goal:
        # 현재 단어가 cards1과 cards2 양쪽에 있는 경우, 순서를 고려하여 선택합니다.
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1  # cards1에서 단어를 선택하고 인덱스를 증가시킵니다.
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1  # cards2에서 단어를 선택하고 인덱스를 증가시킵니다.
        else:
            return "No"  # 목표 단어를 만들 수 없는 경우
    return "Yes"  # 모든 단어를 순서대로 선택할 수 있는 경우