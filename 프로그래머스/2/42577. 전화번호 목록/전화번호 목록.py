def solution(phone_book):
    # 전화번호 정렬
    phone_book.sort()
    
    # 인접한 전화번호끼리 접두어 관계 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True
