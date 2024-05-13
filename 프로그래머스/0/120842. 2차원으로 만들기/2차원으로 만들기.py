def solution(num_list, n):
    answer = []
    ans = []
    for num in num_list:
        if len(ans) == n :
            answer.append(ans)
            ans = []
            ans.append(num)
        else:
            ans.append(num)
    answer.append(ans)
    return answer