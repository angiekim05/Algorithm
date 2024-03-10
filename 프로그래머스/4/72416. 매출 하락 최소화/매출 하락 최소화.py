def solution(sales, links):
    def dfs(x):
        dp[x][1] = sales[x-1]
        if not g[x]:
            return
        k_min = 0
        attend = False
        for k in g[x]:
            dfs(k)
            if dp[k][0] <= dp[k][1]:
                k_min += dp[k][0]
            else:
                attend = True
                k_min += dp[k][1]
        dp[x][1] += k_min
        dp[x][0] += k_min
        if not attend:
            dp[x][0] += min([dp[r][1] - dp[r][0] for r in g[x]])




    n = len(sales)
    dp = [[0, 0] for _ in range(n+1)]
    g = {i:[] for i in range(n+1)}
    for a, b in links:
        if a in g:
            g[a].append(b)
        else:
            g[a] = [b]
    dfs(1)
    answer = min(dp[1])
    return answer