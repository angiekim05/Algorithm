def solution(dirs):
    dir = {"U":(-1,0),"D":(1,0),"R":(0,1),"L":(0,-1)}
    answer = set()
    x,y = 0,0
    for d in dirs:
        dx,dy = dir[d]
        nx,ny = x+dx, y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            answer.add(tuple(sorted([(x,y),(nx,ny)])))
            x,y = nx,ny
    return len(answer)