def solution(dots):
    dots.sort() 
    slope1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    slope2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    if slope1 == slope2:
        return 1
    else:
        return 0
