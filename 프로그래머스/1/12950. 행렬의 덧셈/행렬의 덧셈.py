def solution(arr1, arr2):
    answer = []
    for array in range(len(arr1)):
        arr_check = []
        for arr in range(len(arr1[array])):
            arr_check.append(arr1[array][arr] + arr2[array][arr])
        answer.append(arr_check)
        
    return answer