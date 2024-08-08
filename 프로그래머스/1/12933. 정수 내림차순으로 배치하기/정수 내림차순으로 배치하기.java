import java.util.Arrays;

class Solution {
    public long solution(long n) {
        String numStr = Long.toString(n);
        char[] chars = numStr.toCharArray();
        Arrays.sort(chars);
        String sortedNumStr = new StringBuilder(new String(chars)).reverse().toString();
        
        return Long.parseLong(sortedNumStr);
    }
}