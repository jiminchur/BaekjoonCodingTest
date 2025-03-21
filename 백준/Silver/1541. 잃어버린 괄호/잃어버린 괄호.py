import sys

def min_calcul(expression):
    numbers = expression.split('-')  # '-' 기준으로 나누기
    result = sum(map(int, numbers[0].split('+')))  # 첫 번째 부분 합산(무조건 더함)

    for num in numbers[1:]:
        result -= sum(map(int, num.split('+')))  # 그 뒤로 나오는 모든 숫자들은 빼줌

    return result

# 입력 처리
cal = sys.stdin.readline().strip()
print(min_calcul(cal))