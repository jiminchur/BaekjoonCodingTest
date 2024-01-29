def solution(s):
    answer = ''
    sol_ = s.lower()
    sol = sol_.split(" ")
    lst = []
    for i in sol :
        lst.append(i.capitalize())
    answer = " ".join(lst)
    return answer