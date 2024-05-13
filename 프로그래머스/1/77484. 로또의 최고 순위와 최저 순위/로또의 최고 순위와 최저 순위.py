def solution(lottos, win_nums):
    answer = []
    count = 0
    best = 0
    for num in lottos:
        if num in win_nums:
            count += 1
        elif num == 0:
            best += 1
    if count + best <= 1:
        answer = [6,6]
    elif count <= 1:
        answer = [7-(count+best),6]
    else :
        answer = [7-(count+best),7-count]
    return answer