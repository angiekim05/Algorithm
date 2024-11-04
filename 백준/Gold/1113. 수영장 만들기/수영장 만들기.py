import sys
input = sys.stdin.readline
import heapq
from collections import deque

n, m = map(int,input().split())
pool = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
min_heap = []
answer = 0

for i in range(n):
    for j in range(m):
        if 1<=i<n-1 and 1<=j<m-1:
            heapq.heappush(min_heap, (pool[i][j],i,j))

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(h,x,y):
    q = deque([(x,y)])
    cnt = 1
    min_height = 10
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx, y+dy

            if not in_range(nx,ny):
                return 0
            if visited[nx][ny]:
                continue
            if pool[x][y] < pool[nx][ny]:
                min_height = min(min_height,pool[nx][ny])
                continue
            if pool[x][y] == pool[nx][ny]:
                cnt += 1
            visited[nx][ny] = 1
            q.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                pool[i][j] = min_height
    return cnt * (min_height-h)

while min_heap:
    h,x,y = heapq.heappop(min_heap)
    if h < pool[x][y]:
        continue
    answer += bfs(h,x,y)

print(answer)