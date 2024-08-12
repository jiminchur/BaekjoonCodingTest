class Solution {
    public String solution(String[] seoul) {
          // "Kim"의 위치를 찾기
        int x = -1; // 초기값 설정
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                x = i; // "Kim"의 위치를 저장
                break; // 찾았으므로 루프 종료
            }
        }
        
        // 결과 문자열 반환
        return "김서방은 " + x + "에 있다";
    }
}