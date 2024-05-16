def solution(keyinput, board):
    answer = [0,0]
    dic = {"left":[-1,0], "right":[1,0], "up":[0,1], "down":[0,-1]}
    for i in keyinput :
        x,y = dic[i]
        if -(board[0] // 2) <= answer[0] + x <= board[0] // 2 and -(board[1] // 2) <= answer[1] + y <= board[1] // 2:
            answer[0] += x
            answer[1] += y
        
    return answer