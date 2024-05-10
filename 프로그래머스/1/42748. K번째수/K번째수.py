def solution(array, commands):
    answer = []
    for command in commands:
        if command[0] == command[1]:
            command_array = [array[command[0]-1]]
        else :
            command_array = array[command[0]-1:command[1]]
        command_array.sort()
        answer.append(command_array[command[2]-1])        
    return answer