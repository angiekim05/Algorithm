import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def check_area(i,j):
    before_color = arr1[i][j]
    after_color = arr2[i][j]
    q = deque([(i,j)])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy

            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if arr1[nx][ny] == before_color:
                if arr2[nx][ny] == after_color:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                else: # 모든 영역이 같은 값으로 업데이트되지 않으면 CPCU-1202 백신이 아님
                    print("NO")
                    exit()
    return before_color == after_color

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if not check_area(i,j):
                cnt += 1
if cnt > 1:
    print("NO")
else:
    print("YES")