def solution(survey, choices):
    lst = ["R","T","C","F","J","M","A","N"]
    dic = {}
    answer = ''
    
    for mbti in lst:
        dic[mbti] = 0
        
    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
            
    for check in range(0,8,2):
        if dic[lst[check]] >= dic[lst[check+1]]:
            answer += lst[check]
        elif dic[lst[check]] < dic[lst[check+1]]:
            answer += lst[check+1]
        

    return answer