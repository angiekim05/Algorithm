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
                else:
                    # 치즈 녹임
                    arr[nx][ny] = 0
    return

def melt():
    # 녹기 전 치즈 조각 수
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
    # 치즈 녹이기
    bfs(0,0)
    return cnt

ans = [0,0]
while True:
    # 녹기 전 치즈 조각 수
    cnt = melt()
    # 치즈가 다 녹았다면 멈춤
    if cnt == 0:
        break
    ans[0] += 1 # 시간 지남
    ans[1] = cnt

print(*ans,sep="\n")