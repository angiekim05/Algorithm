from itertools import product
    
def solution(users, emoticons):
    answer = [0,0]
    n,m = len(users),len(emoticons)
    for e_h in product([6,7,8,9], repeat = m):
        new, total = 0,0
        e_c = [emoticons[i] * e_h[i] // 10 for i in range(m)]
        for u_h,u_c in users:
            cost = 0
            for idx, c in enumerate(e_c):
                if u_h <= (10-e_h[idx])*10:
                    cost += c

            if cost >= u_c:
                new+=1
            else:
                total+= cost
                
        if answer[0] < new:
            answer = [new, total]
        elif answer[0] == new and answer[1] < total:
            answer = [new, total]

    return answer