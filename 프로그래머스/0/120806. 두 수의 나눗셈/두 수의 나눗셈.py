def solution(num1, num2):
    _answer = (num1 / num2) * 1000
    answer = str(_answer).split(".")[0]
    return int(answer)