def find_receivers(heights):
    stack = []  # (index, height)
    result = [0] * len(heights)

    for i in range(len(heights)):
        while stack and stack[-1][1] < heights[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1][0] + 1  # +1은 인덱스를 탑 번호로 맞추기 위해
        
        stack.append((i, heights[i]))
    
    return result

# 입력 처리
import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

# 결과 출력
print(' '.join(map(str, find_receivers(heights))))