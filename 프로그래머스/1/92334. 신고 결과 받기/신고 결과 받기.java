import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        // 유저별 신고 정보 저장 (중복 방지를 위해 HashSet 사용)
        Map<String, HashSet<String>> reports = new HashMap<>();

        // 유저별 결과 메일 수신 횟수 저장
        Map<String, Integer> mailCount = new HashMap<>();

        // 초기화
        for (String user: id_list) {
            reports.put(user, new HashSet<>());
            mailCount.put(user, 0);
        }

        // 신고 정보 저장
        for (String r: report) {
            String[] splitReport = r.split(" ");
            String reporter = splitReport[0]; // 신고자
            String reported = splitReport[1]; // 피신고자

            reports.get(reported).add(reporter);
        }

        // k번 이상 신고인지 확인하고 메일 보내기
        for (String reportedUser: reports.keySet()) {
            HashSet<String> reporters = reports.get(reportedUser);
            if (reporters.size() >= k) {
                // 신고자에게 메일 보내기
                for (String reporter: reporters) {
                    mailCount.put(reporter, mailCount.get(reporter)+1);
                }
            }
        }

        // 결과를 배열로 반환
        int[] answer = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = mailCount.get(id_list[i]);
        }
        return answer;
    }
}
