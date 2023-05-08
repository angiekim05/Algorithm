import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
arr = list(map(int,input().split()))

for i in range(1,1+n):
    dp[i] = arr[i-1]
    for j in range(i//2+1):
        dp[i] = min(dp[i],dp[j]+dp[i-j])

print(dp[-1])