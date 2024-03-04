import heapq
def solution(n, s, a, b, fares):
    def dijkstra(s):
        hq = [(0,s)]
        cost = [float("inf")]*(n+1)
        while hq:
            c,x = heapq.heappop(hq)
            
            if cost[x] < c:
                continue
            
            for nx,nc in g[x]:
                if cost[nx] > c + nc:
                    cost[nx] = c + nc
                    heapq.heappush(hq,(c+nc, nx))
        return cost
    
    g = dict()
    for start, end, fare in fares:
        if start in g:
            g[start].append((end,fare))
        else:
            g[start] = [(end,fare)]
                    
        if end in g:
            g[end].append((start,fare))
        else:
            g[end] = [(start,fare)]
            
    from_start_to = dijkstra(s)
    from_a_to = dijkstra(a)
    from_b_to = dijkstra(b)
    bridge = [from_start_to[i]+from_a_to[i]+from_b_to[i] for i in range(n+1)]
    seperate = from_start_to[a]+from_start_to[b]
    through_a = from_start_to[a] + from_b_to[a]
    through_b = from_start_to[b] + from_a_to[b]
    answer = min(seperate,*bridge,through_a,through_b)
        
    return answer