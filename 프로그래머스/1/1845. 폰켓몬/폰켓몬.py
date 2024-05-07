def solution(nums):
    nums_half = len(nums) // 2
    no_sames_counts = len(set(nums))
    if nums_half >= no_sames_counts :
        answer = no_sames_counts
    elif nums_half < no_sames_counts :
        answer = nums_half
    return answer