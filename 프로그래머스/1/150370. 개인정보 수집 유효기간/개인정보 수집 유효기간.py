# 날짜를 일수로 변환
def to_days(date):
    y, m, d = map(int, date.split("."))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    answer = []
    today = to_days(today)
    
    # 약관 정보
    term = dict()
    for t in terms:
        type_, period = t.split()
        term[type_] = int(period)*28
    
    # 개인정보 만료기간과 오늘 일수를 비교하여 파기 목록에 추가
    for idx, p in enumerate(privacies):
        numb = idx+1
        date, type_ = p.split()
        
        # 오늘보다 만료기간이 짧으면 파기해야 한다.
        if to_days(date) + term[type_] -1 < today:
            answer.append(numb)
    
    return answer