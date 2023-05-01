def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        n,m = 0,0
        temp = cap
        while deliveries:
            d = deliveries.pop()
            if d == 0:
                continue
            n = max(n,len(deliveries)+1)
            if d <= temp:
                temp -= d
            else:
                deliveries.append(d-temp)
                break
        temp = cap
        while pickups:
            p = pickups.pop()
            if p == 0:
                continue
            m = max(m,len(pickups)+1)
            if p <= temp:
                temp -= p
            else:
                pickups.append(p-temp)
                break
        
        answer += max(n,m)*2

        
    return answer