def solution(answers):
    answer_ = []
    student_1 = [1,2,3,4,5]*2000
    student_1_correct = 0
    student_2 = [2,1,2,3,2,4,2,5]*1250
    student_2_correct = 0
    student_3 = [3,3,1,1,2,2,4,4,5,5]*1000
    student_3_correct = 0
    for answer in range(len(answers)):
        if answers[answer] == student_1[answer]:
            student_1_correct += 1
        if answers[answer] == student_2[answer]:
            student_2_correct += 1
        if answers[answer] == student_3[answer]:
            student_3_correct += 1            
    best_correct = max(student_1_correct,student_2_correct,student_3_correct)
    if best_correct == student_1_correct:
        answer_.append(1)
    if best_correct == student_2_correct:
        answer_.append(2)
    if best_correct == student_3_correct:
        answer_.append(3)
    return answer_