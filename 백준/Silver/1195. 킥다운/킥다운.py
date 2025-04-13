def is_compatible(g1, g2, offset):
    """
    offset: g2가 g1보다 오른쪽으로 얼마나 이동했는지
    """
    for i in range(len(g2)):
        if 0 <= offset + i < len(g1):
            if g1[offset + i] == '2' and g2[i] == '2':
                return False
    return True

def min_width(g1, g2):
    min_len = len(g1) + len(g2)
    
    # g2가 g1 왼쪽으로 겹칠 수도 있음 (offset < 0)
    for offset in range(-len(g2), len(g1) + 1):
        if is_compatible(g1, g2, offset):
            left = min(offset, 0)
            right = max(len(g1), offset + len(g2))
            min_len = min(min_len, right - left)
    
    return min_len

# 입력
g1 = input().strip()
g2 = input().strip()

# 출력
print(min_width(g1, g2))