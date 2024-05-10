def solution(sizes):
    Max_sizes = []
    Min_sizes = []
    for size in sizes:
        Max_sizes.append(max(size))
        Min_sizes.append(min(size))
    answer = max(Max_sizes)*max(Min_sizes)
    return answer