import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        List<Character> allList = new ArrayList<>();
        
        // 알파벳 a-z를 리스트에 추가
        for (char c = 'a'; c <= 'z'; c++) {
            allList.add(c);
        }

        for (char k : s.toCharArray()) {
            int currentIndex = allList.indexOf(k);
            int steps = index;

            // 다음 인덱스를 찾기 위한 반복
            while (steps > 0) {
                currentIndex = (currentIndex + 1) % allList.size();
                // skip에 포함되지 않은 경우에만 steps 감소
                if (skip.indexOf(allList.get(currentIndex)) == -1) {
                    steps--;
                }
            }

            answer.append(allList.get(currentIndex));
        }
        
        return answer.toString();
    }
}
