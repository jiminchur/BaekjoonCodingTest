from itertools import permutations

def solution(k, dungeons):
    max_count = 0  # 탐험할 수 있는 최대 던전 수
    # 모든 던전 탐험 순서의 순열 생성
    for dungeon_order in permutations(dungeons, len(dungeons)):
        fatigue = k  # 초기 피로도 설정
        count = 0  # 현재 순서로 탐험할 수 있는 던전 수
        # 생성된 순서대로 던전 탐험 시도
        for min_fatigue, consume_fatigue in dungeon_order:
            # 현재 피로도로 탐험 가능한 경우
            if fatigue >= min_fatigue:
                fatigue -= consume_fatigue  # 피로도 소모
                count += 1  # 탐험한 던전 수 증가
            else:
                break  # 더 이상 탐험 불가능
        max_count = max(max_count, count)  # 최대 탐험 가능 던전 수 갱신
    return max_count
