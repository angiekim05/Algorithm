n,m = map(int,input().split())
r,c,d = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def cleaner(x,y,d):
    # 현재칸 청소
    cnt = 1
    area[x][y] = -1
    while True:
        # 반시계 방향으로 회전하며 청소하지 않은 칸 탐색
        for _ in range(4):
            d = (d - 1) % 4
            nx,ny = x+dx[d], y+dy[d]
            if area[nx][ny] == 0: # 청소 안한 칸
                area[nx][ny] = -1
                cnt += 1
                x,y = nx,ny
                break # 청소했으면 다시 1번으로 돌아감

        else:
            # 청소 못했으면 후진하거나 멈추거나
            x,y = x+dx[d]*(-1), y+dy[d]*(-1)
            if area[x][y] == 1: # 벽이라면 작동 멈춤
                return cnt

print(cleaner(r,c,d))