def solution(friends, gifts):
    n = len(friends)
    answer = [0]*n
    name2idx = {name:idx for idx,name in enumerate(friends)}
    
    p = [[0]*n for _ in range(n)]
    # 준 선물 체크 (row) -> col은 받은 선물이 됨
    for ab in gifts:
        a,b = ab.split()
        p[name2idx[a]][name2idx[b]] += 1
    
    # 선물지수
    score = [0]*n
    for a in range(n):
        for b in range(n):
            score[a] += p[a][b] # 준선물
            score[b] -= p[a][b] # 받은선물
            
    for a in range(n):
        for b in range(a+1,n):
            if p[a][b] > p[b][a]:
                answer[a] += 1
            elif p[a][b] < p[b][a]:
                answer[b] += 1
            else:
                if score[a] > score[b]:
                    answer[a] += 1
                elif score[b] > score[a]:
                    answer[b] += 1
            
    
    return max(answer)