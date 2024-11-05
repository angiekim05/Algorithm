import heapq

n, m = map(int,input().split())
pool = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def solution():
    min_heap = []
    answer = 0

    # 외곽부터 탐색
    for i in range(n):
        for j in range(m):
            if 1<=i<n-1 and 1<=j<m-1:
                continue
            heapq.heappush(min_heap, (pool[i][j],i,j))
            visited[i][j] = 1

    while min_heap:
        h,x,y = heapq.heappop(min_heap)

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx, y+dy

            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if h > pool[nx][ny]:
                answer += h-pool[nx][ny]
                pool[nx][ny] = h
            heapq.heappush(min_heap,(pool[nx][ny],nx,ny))
            visited[nx][ny] = 1

    print(answer)

solution()