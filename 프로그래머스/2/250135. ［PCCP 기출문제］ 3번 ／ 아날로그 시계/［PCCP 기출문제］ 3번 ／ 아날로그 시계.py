def solution(h1, m1, s1, h2, m2, s2):
    def count(h,m,s):
        dh = 60 * h + m - (2 if h >= 12 else 0)
        dm = 59 * h + m 
        return dh + dm - 1 + last_min(h,m,s)
    
    def last_min(h,m,s):
        cnt = 0
        dh = (3600 * h + 60 * m + s)%43200
        dm = (60 * 12 * m + 12 * s)%43200
        ds = (720 * s)%43200
        if ds >= dh:
            cnt += 1
        if ds >= dm:
            cnt += 1
        return cnt
    
    bf = count(h1,m1,s1)
    af = count(h2,m2,s2) 
    
    if (h1,m1,s1) in [(0,0,0),(12,0,0)]:
        af += 1
        
    return af-bf 