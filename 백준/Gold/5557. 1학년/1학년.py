import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n)]
dp[0][arr[0]] = 1 # 맨 처음 주어진 숫자 표시 -> 가능한 경우의 수 1
for i in range(n-2):
    for j in range(21):
        # 만약 j 숫자가 앞서 만들어 질 수 있는 숫자라면
        if dp[i][j] != 0:
            # 다음 숫자 arr[i+1]에 현재 합 j가 더해져도 0이상 20이하이면 경우의 수 추가
            if 0 <= j + arr[i + 1] <= 20:
                dp[i + 1][j + arr[i + 1]] += dp[i][j]
            # -기호 일 경우도 확인
            if 0 <= j - arr[i + 1] <= 20:
                dp[i + 1][j - arr[i + 1]] += dp[i][j]

# 마지막 값과 총합이 같은 경우의 수 출력
print(dp[-2][arr[-1]])