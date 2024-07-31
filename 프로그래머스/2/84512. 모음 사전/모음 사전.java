import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public int solution(String word) {
        List<String> words = new ArrayList<>();

        for (int i = 1; i <= 5; i++) {
            generateWords("", i, words);
        }

        Collections.sort(words);

        return words.indexOf(word) + 1;
    }

    private void generateWords(String current, int length, List<String> words) {
        if (length == 0) {
            words.add(current);
            return;
        }
        char[] chars = {'A', 'E', 'I', 'O', 'U'};

        for (char c : chars) {
            generateWords(current + c, length - 1, words);
        }
    }
}
