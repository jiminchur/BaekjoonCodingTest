def solution(s):
    answer = 0
    lst = s.split(' ')
    for i in range(lst.__len__()):
        if lst[i] == "Z":
            answer -= int(lst[i-1])
        else:
            answer += int(lst[i])
    return answer