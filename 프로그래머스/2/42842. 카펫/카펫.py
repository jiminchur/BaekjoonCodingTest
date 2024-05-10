def comb(count):
    ab_lst = []
    if count % 2 == 0:
        for i in range(1,count//2+1):
            if count%i == 0:
                ab_lst.append([i,count//i])
    elif count == 1:
        ab_lst.append([1,1])
    else :
        for i in range(1,count//2+1):
            if count%i == 0:
                ab_lst.append([i,count//i])
    return ab_lst

def solution(brown, yellow):
    answer = []
    a_b = (brown-4)/2
    ab_lst = comb(yellow)
    for comb_ab in ab_lst:
        if comb_ab[0]+comb_ab[1] == a_b:
            answer.append(comb_ab[1]+2)
            answer.append(comb_ab[0]+2)
            break
    return answer