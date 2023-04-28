def solution(n, stations, w):
    ans,x,idx = 0,1,0
    area = 2*w+1
    while x <= n:
        if idx < len(stations) and x >= stations[idx]-w:
            x = stations[idx]+w+1
            idx += 1
        else:
            x += area
            ans += 1
    return ans