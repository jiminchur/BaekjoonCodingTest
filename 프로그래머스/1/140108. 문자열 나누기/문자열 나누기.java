public class Solution {
    public int solution(String s) {
        char[] lst = s.toCharArray(); 
        int count = 0; 
        int answer = 0; 
        char check = '\0'; 

        for (char i : lst) {
            if (count == 0 || check == i) {
                check = i; 
                count++; 
            } else {
                count--; 
                if (count == 0) {
                    answer++; 
                }
            }
        }

        if (count > 0) {
            answer++; 
        }
        
        return answer;
    }
}
