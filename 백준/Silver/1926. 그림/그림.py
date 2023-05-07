import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(i,j):
    s = [(i,j)]
    visited[i][j] = 1
    area = 1
    while s:
        x,y = s.pop()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx, y+dy
            if 0<= nx < n and 0<= ny < m:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    area += 1
                    s.append((nx,ny))
    return area
cnt = 0
area = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            area = max(area,dfs(i,j))
            cnt += 1

print(cnt)
print(area)