import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = []
q = deque()
ans = [[-1]*m for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j,0))
            ans[i][j] = 0
        elif arr[i][j] == 0:
            ans[i][j] = 0

while q:
    x,y,d = q.popleft()
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if ans[nx][ny] == -1:
                ans[nx][ny] = d+1
                q.append((nx,ny,d+1))
for i in range(n):
    print(*ans[i])
