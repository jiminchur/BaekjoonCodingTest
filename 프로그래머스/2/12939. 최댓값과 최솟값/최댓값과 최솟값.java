class Solution {
    public String solution(String s) {
        String[] lst = s.split(" ");  // 문자열을 공백으로 분리
        int[] lst2 = new int[lst.length];
        
        // 문자열을 정수로 변환하여 배열에 저장
        for (int i = 0; i < lst.length; i++) {
            lst2[i] = Integer.parseInt(lst[i]);
        }
        
        // 최대값과 최소값 찾기
        int max = lst2[0];
        int min = lst2[0];
        for (int num : lst2) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        
        // 결과 문자열 생성
        return min + " " + max;
    }
}