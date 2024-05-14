def solution(k, score):
    answer = []
    best_score = []
    for i in score :
        if len(best_score) < k:
            best_score.append(i)
            best_score.sort()
            best_score.reverse()
            answer.append(best_score[-1])
        elif len(best_score) == k:
            if best_score[-1] < i:
                best_score.append(i)
                best_score.sort()
                best_score.reverse()
                del best_score[-1]
                answer.append(best_score[-1])
            else :
                answer.append(best_score[-1])
    return answer