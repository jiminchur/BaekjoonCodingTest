from itertools import permutations

def solution(spell, dic):
    answer = 0
    lst = []
    for k in permutations(spell):
        lst.append("".join(k))
    for dicc in dic :
        if dicc in lst:
            return 1
        
    return 2