class Solution {
    public int solution(int[] a, int[] b) {
        int dotProduct = 0;
        
        // 배열의 길이를 기반으로 내적 계산
        for (int i = 0; i < a.length; i++) {
            dotProduct += a[i] * b[i];
        }
        
        return dotProduct;
    }
}