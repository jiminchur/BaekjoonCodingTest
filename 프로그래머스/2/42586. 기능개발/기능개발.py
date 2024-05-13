def solution(progresses, speeds):
    answer = []
    while True :
        if len(progresses) == 0:
            break
            
        for work in range(len(progresses)):
            progresses[work] += speeds[work]
            if progresses[work] >= 100:
                progresses[work] = 100
                
        count = 0
        while progresses and progresses[0] == 100: 
            count += 1
            del progresses[0]
            del speeds[0]  
            
        if count > 0:  
            answer.append(count)


    return answer