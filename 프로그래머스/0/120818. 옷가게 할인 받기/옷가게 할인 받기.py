def solution(price):
    dis = 0
    if price >= 500000:
        dis = 0.2
    elif price >= 300000:
        dis = 0.1
    elif price >= 100000:
        dis = 0.05
    
    disprice = price * dis
    answer = price - disprice
    
    return int(answer)
