import sys

def main():
    # 입력: n(총 돈), m(생명체 수)
    n_str, m_str = sys.stdin.readline().split()
    
    # Python int는 큰 수도 자동으로 처리
    n = int(n_str)
    m = int(m_str)
    
    # 한 생명체당 받을 수 있는 돈
    quotient = n // m
    # 남는 돈
    remainder = n % m
    
    print(quotient)
    print(remainder)

if __name__ == "__main__":
    main()