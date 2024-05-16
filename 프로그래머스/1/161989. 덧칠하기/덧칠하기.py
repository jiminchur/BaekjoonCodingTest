def solution(n, m, section):
    if not section: 
        return 0

    paint_count = 1
    end = section[0] + m - 1

    for i in range(1, len(section)):
        if section[i] > end:
            paint_count += 1
            end = section[i] + m - 1

    return paint_count
