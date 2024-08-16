class Solution {
    public String solution(String phone_number) {
        int length = phone_number.length();
        
        // 뒷 4자리를 제외한 부분을 *로 가리기
        StringBuilder maskedNumber = new StringBuilder();
        
        for (int i = 0; i < length - 4; i++) {
            maskedNumber.append('*');
        }
        
        // 뒷 4자리 추가
        maskedNumber.append(phone_number.substring(length - 4));
        
        return maskedNumber.toString();
    }
}