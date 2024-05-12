def solution(my_string):
    my_string_lst = my_string.split(" ")
    check = int(my_string_lst[0])
    for num in range(2,len(my_string_lst)):
        if my_string_lst[num] == "+" or my_string_lst[num] == "-":
            pass
        elif int(my_string_lst[num]):
            if my_string_lst[num-1] == "+":
                check += int(my_string_lst[num])
            elif my_string_lst[num-1] == "-":
                check -= int(my_string_lst[num])
    answer = check
    return answer