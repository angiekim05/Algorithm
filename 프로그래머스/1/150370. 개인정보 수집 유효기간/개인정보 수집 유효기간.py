def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split("."))
    today = y*12*28 + m*28 + d
    
    term = dict()
    for t in terms:
        type_, period = t.split()
        term[type_] = int(period)
    
    for idx, p in enumerate(privacies):
        numb = idx+1
        date, type_ = p.split()
        y, m, d = map(int, date.split("."))
        m += term[type_]
        
        if y*12*28 + m*28 + d <= today:
            answer.append(numb)
    
    return answer