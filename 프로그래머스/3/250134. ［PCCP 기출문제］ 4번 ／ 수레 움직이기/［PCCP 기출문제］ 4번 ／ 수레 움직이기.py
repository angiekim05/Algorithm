def solution(maze):
    global answer
    answer = 100
    n,m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i,j)
            elif maze[i][j] == 2:
                blue_start = (i,j)
            elif maze[i][j] == 3:
                red_end = (i,j)
            elif maze[i][j] == 4:
                blue_end = (i,j)
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    red, blue = 0,1
    visited[red_start[0]][red_start[1]][red] = 1
    visited[blue_start[0]][blue_start[1]][blue] = 1
    
    
    def in_range(x,y):
        if not (0<=x<n and 0<=y<m):
            return False
        return maze[x][y] != 5
    
    def dfs(cnt,rx,ry,bx,by,rgoal,bgoal):
        global answer
        if rgoal and bgoal:
            answer = min(answer,cnt)
            return
        if cnt > answer:
            return
        for i in range(4):
            for j in range(4):
                if not rgoal:
                    nrx,nry = rx+dx[i], ry+dy[i]
                else:
                    nrx,nry = rx,ry
                if not bgoal:
                    nbx,nby = bx+dx[j], by+dy[j]
                else:
                    nbx,nby = bx,by
                if not in_range(nrx,nry) or not in_range(nbx,nby):
                    continue
                if (nrx,nry) == (nbx,nby):
                    continue
                if (nrx, nry) == (bx, by) and (nbx,nby) == (rx,ry):
                    continue
                if not rgoal and visited[nrx][nry][red]:
                    continue
                if not bgoal and visited[nbx][nby][blue]:
                    continue
                visited[nrx][nry][red] = 1
                visited[nbx][nby][blue] = 1
                if rgoal or (nrx, nry) == red_end:
                    nrgoal = True
                else:
                    nrgoal = False
                if bgoal or (nbx,nby) == blue_end:
                    nbgoal = True
                else:
                    nbgoal = False
                dfs(cnt+1,nrx,nry,nbx,nby,nrgoal,nbgoal)
                visited[nrx][nry][red] = 0
                visited[nbx][nby][blue] = 0
                
    dfs(0,red_start[0],red_start[1],blue_start[0],blue_start[1],False,False)
    return 0 if answer == 100 else answer