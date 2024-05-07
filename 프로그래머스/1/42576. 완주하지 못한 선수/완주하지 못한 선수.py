from collections import Counter

def solution(participant, completion):
    dic = Counter(participant) - Counter(completion)
    answer = list(dic.elements())[0]
    return answer