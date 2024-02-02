def solution(operations):
    lst = []
    for i in operations:
        if "I" in i:
            a,b = i.split(" ")
            lst.append(int(b))
        elif i == "D 1" :
            if lst.__len__() > 0:
                k = max(lst)
                lst.remove(k)
            else :
                pass
        elif i == "D -1" :
            if lst.__len__() > 0:
                k2 = min(lst)
                lst.remove(k2)
            else : 
                pass
    if lst.__len__() == 0 :
        answer = [0,0]
    elif lst.__len__() >= 2 :
        answer = [max(lst),min(lst)]
    return answer