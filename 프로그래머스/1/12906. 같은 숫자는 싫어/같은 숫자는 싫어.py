def solution(arr):
    lst = []
    for i in arr:
        if lst.__len__() == 0:
            lst.append(i)
        elif lst[-1] != i:
            lst.append(i)
    return lst