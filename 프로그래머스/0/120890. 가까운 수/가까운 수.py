def solution(array, n):
    differences = [abs(x - n) for x in array]
    min_diff = min(differences)
    closest = [array[i] for i, diff in enumerate(differences) if diff == min_diff]
    return min(closest)
