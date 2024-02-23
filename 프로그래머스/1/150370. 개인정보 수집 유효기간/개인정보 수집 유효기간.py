def solution(today, terms, privacies):
    answer = []
    yyyy, mm, dd = map(int, today.split("."))
    
    term = dict()
    for t in terms:
        type_, period = t.split()
        term[type_] = int(period)
    
    for idx, p in enumerate(privacies):
        numb = idx+1
        date, type_ = p.split()
        y, m, d = map(int, date.split("."))
        temp,m = divmod(m+term[type_],12)
        y += temp
        if m == 0:
            m = 12
            y -= 1
        if yyyy > y:
            answer.append(numb)
        elif yyyy == y:
            if mm > m:
                answer.append(numb)
            elif mm == m:
                if dd >= d:
                    answer.append(numb)
    
    return answer