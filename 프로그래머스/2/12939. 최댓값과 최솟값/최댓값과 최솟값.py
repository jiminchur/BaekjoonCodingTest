def solution(s):
    answer = ''
    lst = s.split(" ")
    lst2 = []
    for i in lst:
        lst2.append(int(i))
    a = max(lst2)
    b = min(lst2)
    answer = str(b) + " " + str(a)
    return answer