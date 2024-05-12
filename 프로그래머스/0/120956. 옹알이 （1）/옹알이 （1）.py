from itertools import permutations

def solution(babbling):
    babbling_lst = ["aya", "ye", "woo", "ma"]
    count = 0
    all_babbling_lst = []
    for length in range(1,5):
        for permu in permutations(babbling_lst,length):
            all_babbling_lst.append("".join(permu))
    
    for speak in babbling:
        if speak in all_babbling_lst:
            count += 1
    answer = count
    return answer