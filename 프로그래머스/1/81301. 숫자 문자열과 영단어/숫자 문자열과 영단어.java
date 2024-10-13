import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String s) {
        // 영단어-숫자 HashMap
        Map<String, String> numMap = new HashMap<>();
        numMap.put("zero", "0");
        numMap.put("one", "1");
        numMap.put("two", "2");
        numMap.put("three", "3");
        numMap.put("four", "4");
        numMap.put("five", "5");
        numMap.put("six", "6");
        numMap.put("seven", "7");
        numMap.put("eight", "8");
        numMap.put("nine", "9");

        for (String word : numMap.keySet()) {
            s = s.replace(word, numMap.get(word));
        }

        int answer = Integer.parseInt(s);
        return answer;
    }
}