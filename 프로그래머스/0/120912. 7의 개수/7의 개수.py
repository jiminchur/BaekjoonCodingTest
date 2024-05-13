def solution(array):
    str_array = "".join(list(map(str,array)))
    answer = str_array.count("7")
    return answer