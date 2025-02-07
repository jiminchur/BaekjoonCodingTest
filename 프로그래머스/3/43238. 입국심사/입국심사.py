def solution(n, times):
    left, right = 1, max(times) * n  # 최소 시간과 최대 시간 설정
    answer = right  

    while left <= right:
        mid = (left + right) // 2  # 중간 시간 기준으로 심사가 가능한지 확인
        people_checked = sum(mid // time for time in times)  # 해당 시간 동안 심사 가능한 총 인원

        if people_checked >= n:  # 필요한 인원을 충족하면 시간을 줄여본다.
            answer = mid
            right = mid - 1
        else:  # 부족하면 시간을 늘린다.
            left = mid + 1
            
    return answer
