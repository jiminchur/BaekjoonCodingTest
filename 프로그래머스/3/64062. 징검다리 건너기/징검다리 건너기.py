def solution(stones, k):
    left, right = 1, max(stones)  # 최소 1명 ~ 최대 max(stones)명
    answer = 0  

    while left <= right:
        mid = (left + right) // 2  # 건널 수 있는 최대 인원 수(mid)
        zero_count = 0  # 연속된 0 개수
        max_zero_count = 0  # k 이상 연속된 0이 있는지 확인
        
        for stone in stones:
            if stone < mid:  # mid명이 건넜을 때, 돌이 0 이하가 되는 경우
                zero_count += 1
                if zero_count >= k:  # 연속된 0이 k 이상이면 못 건넘
                    break
            else:
                zero_count = 0  # 연속된 0이 끊김

        if zero_count >= k:  # k 이상 연속된 0이 있으면 불가능
            right = mid - 1  
        else:  # 건널 수 있으면 더 큰 값 탐색
            left = mid + 1
            answer = mid  # 가능한 최대 인원 업데이트
    
    return answer
