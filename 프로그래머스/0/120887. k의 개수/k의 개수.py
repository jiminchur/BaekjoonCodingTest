def solution(i, j, k):
    i_j_lst = list(map(str,range(i,j+1)))
    i_j = "".join(i_j_lst)
    answer = i_j.count(str(k))
    return answer