from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def bfs(i,j):
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]:
                    continue
                # 방문하지 않은 곳은 방문 체크
                # 즉 치즈가 없는 공기와 공기와 맞닿은 치즈를 방문 체크
                visited[nx][ny] = 1
                # 치즈가 없는 곳으로 이동
                if arr[nx][ny] == 0:
                    q.append((nx,ny))
    return visited

def melt():
    new = [[0]*m for _ in range(n)]
    visited = bfs(0,0)
    # visited는 공기와 공기와 맞닿은 치즈임으로
    # 방문하지 않은 곳 중 치즈가 있는 곳이 아직 치즈가 녹지 않고 남은 곳임
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                cnt += 1
                new[i][j] = 1
    return new,cnt

ans = [0,0]
# 초기 치즈 조각 수
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans[1] += 1

while True:
    # 녹은 후 새로운 arr와 치즈 조각 수
    arr,cnt = melt()
    ans[0] += 1

    # 치즈가 다 녹았다면 멈춤
    if cnt == 0:
        break

    ans[1] = cnt

print(ans[0])
print(ans[1])