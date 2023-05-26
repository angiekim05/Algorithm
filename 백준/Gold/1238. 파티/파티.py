from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n,m,x = map(int, input().split())
d = {i+1:[] for i in range(n)}
for i in range(m):
    a,b,c = map(int, input().split())
    d[a].append((b,c))

def bfs_from_x(i):
    visited = [float("inf")]*(n+1)
    visited[i] = 0
    q = [(0,i)]
    while q:
        t,now = heappop(q)
        if visited[now] > t:
            continue
        for next_,t_ in d[now]:
            if visited[next_] > t+t_:
                visited[next_] = t+t_
                heappush(q,(t+t_,next_))
    return visited

def bfs_from_i(i,x):
    visited = [float("inf")]*(n+1)
    visited[i] = 0
    q = [(0,i)]
    while q:
        t,now = heappop(q)
        if now == x:
            break
        if visited[now] > t:
            continue
        for next_,t_ in d[now]:
            if visited[next_] > t+t_:
                visited[next_] = t+t_
                heappush(q,(t+t_,next_))
    return visited[x]

ans = 0
from_x_to_i = bfs_from_x(x)
for i in range(1,n+1):
    ans = max(ans,bfs_from_i(i,x)+from_x_to_i[i])

print(ans)