def solution(quiz):
    answer = []
    for math in quiz:
        problem = math.split(" ")
        if problem[1] == "+":
            correct_answer = int(problem[0]) + int(problem[2])
        elif problem[1] == "-":
            correct_answer = int(problem[0]) - int(problem[2])
        
        if correct_answer == int(problem[-1]):
            answer.append("O")
        else :
            answer.append("X")
    return answer