class Solution {
    public String solution(int n) {
        StringBuilder result = new StringBuilder();
        
        // "수박" 패턴을 반복하여 추가
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                result.append("수");
            } else {
                result.append("박");
            }
        }
        
        return result.toString();
    }
}