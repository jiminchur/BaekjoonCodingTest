def solution(s):
    answer_n = 1
    answer_m = 0
    while True:
        print(f'현재 s: {s}')
        len_current_s = len(s)
        lst_s = list(s)
        zero_count = lst_s.count("0")
        print(f'0의 개수: {zero_count}')
        
        next_s = len_current_s - zero_count
        answer_m += zero_count
        print(f'0 제거 후 길이(next_s): {next_s}, 누적 제거된 0의 개수(answer_m): {answer_m}')

        if next_s == 1:
            print('next_s가 1이 되어 종료합니다.')
            break
        else:
            s = ""
            original_next_s = next_s
            while True:
                if next_s == 1:
                    s = "1" + s
                    break
                else:
                    remainder = next_s % 2
                    s = str(remainder) + s
                    next_s = next_s // 2
            print(f'{original_next_s}를 이진 변환한 결과 s: {s}')
            answer_n += 1
            print(f'이진 변환 횟수(answer_n): {answer_n}')
    
    return [answer_n, answer_m]
