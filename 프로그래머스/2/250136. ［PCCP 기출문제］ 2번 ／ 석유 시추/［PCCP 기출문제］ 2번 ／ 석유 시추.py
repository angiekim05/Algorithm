def solution(land):
    n,m = len(land), len(land[0])
    answer = [0]*m
    visited = [[0]*m for _ in range(n)]
    
    def in_range(x,y):
        return 0<=x<n and 0<=y<m
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                visited[i][j] = 1
                col = set([j])
                s = [(i,j)]
                cnt = 1
                
                while s:
                    x,y = s.pop()
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx,ny = x+dx,y+dy
                        if not in_range(nx,ny):
                            continue
                        if visited[nx][ny]:
                            continue
                        if land[nx][ny] == 0:
                            continue
                        visited[nx][ny] = 1
                        cnt += 1
                        s.append((nx,ny))
                        col.add(ny)
                
                for c in col:
                    answer[c] += cnt
                    
    return max(answer)