import java.util.Arrays;

public class Solution {

    public static int solution(int[] citations) {
        Arrays.sort(citations);  // 인용 횟수를 오름차순으로 정렬
        int h_index = 0;  // 초기 H-Index 값은 0으로 설정
        
        for (int i = 0; i < citations.length; i++) {
            // 논문의 인덱스(0부터 시작하는 것으로 가정)가 인용 횟수보다 작거나 같으면 H-Index를 업데이트
            if (citations[citations.length - 1 - i] >= (i + 1)) {
                h_index = i + 1;  // H-Index 업데이트
            } else {
                break;  // 논문의 인덱스가 인용 횟수보다 크면 반복을 멈춤
            }
        }
        return h_index;
    }
}
