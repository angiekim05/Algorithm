def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    
    for c in money:
        for x in range(c, n+1):
            dp[x] += dp[x-c] 
    
    return dp[-1]