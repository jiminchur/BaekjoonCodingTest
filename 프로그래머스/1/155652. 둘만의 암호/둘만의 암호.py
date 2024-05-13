def solution(s, skip, index):
    answer = ''
    all_lst = list('abcdefghijklmnopqrstuvwxyz')
    
    for k in s:
        current_index = all_lst.index(k)  
        steps = index 
        
        while steps > 0:
            current_index = (current_index + 1) % len(all_lst) 
            if all_lst[current_index] not in skip:
                steps -= 1  
        
        answer += all_lst[current_index]
    return answer
