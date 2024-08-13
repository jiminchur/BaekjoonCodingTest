import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        
        // divisor로 나누어 떨어지는 요소 찾기
        for (int num : arr) {
            if (num % divisor == 0) {
                list.add(num);
            }
        }
        
        // 요소가 없으면 -1 반환
        if (list.isEmpty()) {
            return new int[]{-1};
        }
        
        // 리스트를 배열로 변환하고 정렬
        int[] result = list.stream().mapToInt(i -> i).toArray();
        Arrays.sort(result);
        
        return result;
    }
}