def solution(hp):
    answer = 0
    big = hp // 5
    medium = (hp % 5) // 3
    small = (hp % 5) % 3
    answer = big + medium + small
    return answer