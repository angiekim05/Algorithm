n = int(input())
wall = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
# dp[row][col][dir]
dp[0][1][0] = 1 # 초기 위치

for i in range(n):
    for j in range(1,n):
        if wall[i][j]:
            continue

        # 오른쪽 이동 : 오른쪽 -> 오른쪽 / 대각선 -> 오른쪽
        dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]

        if i-1 < 0:
            continue
        # 아래쪽 이동 : 아래쪽 -> 아래쪽 / 대각선 -> 아래쪽
        dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]

        if wall[i-1][j] or wall[i][j-1]:
            continue
        # 대각선 이동 : 모든 경우 -> 대각선
        dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))