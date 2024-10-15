import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

# 길이가 1인 경우 팰린드롬 성립
for i in range(n):
    dp[i][i] = 1

# 길이가 2인 경우 두 개의 값이 같아야 팰린드롬 성립
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 길이가 3이상인 경우 양 끝이 같은 값이며, 내부가 팰린드롬이어야 성립
for k in range(2, n): # 팰린드롬 길이
    for i in range(n-k):
        if arr[i] == arr[i+k] and dp[i+1][i+k-1]:
            dp[i][i+k] = 1

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])