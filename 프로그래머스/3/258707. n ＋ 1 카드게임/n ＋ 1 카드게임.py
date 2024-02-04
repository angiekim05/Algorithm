def check_inside(U,tgt):
    for x in list(U):
        diff = tgt - x
        if diff in U:
            return x
    return False
    
def solution(coin, cards):
    answer = 1
    n = len(cards)
    k = n//3
    tgt = n+1
    A = set(cards[:k])
    B = set()
    cango = 0
    
    while k < n:
        
        for a in [cards[k],cards[k+1]]:
            diff = tgt-a
            if diff in A and coin > 0:
                coin -= 1
                cango += 1
                A.remove(diff)
            else:
                B.add(a)
                
        if not cango:
            testa = check_inside(A,tgt)
            if testa:
                cango += 1
                A.remove(testa)
                A.remove(tgt-testa)
            else:
                testb = check_inside(B,tgt)
                if testb and coin >= 2:
                    cango += 1
                    coin -= 2
                    B.remove(testb)
                    B.remove(tgt-testb)
                else:
                    break
                
        cango -= 1
        answer += 1
        k += 2 
    return answer