class Solution {
    public long solution(int a, int b) {
        // a와 b 중 작은 수와 큰 수를 구함
        int start = Math.min(a, b);
        int end = Math.max(a, b);
        
        long sum = 0;
        
        // start부터 end까지의 합을 계산
        for (int i = start; i <= end; i++) {
            sum += i;
        }
        
        return sum;
    }
}