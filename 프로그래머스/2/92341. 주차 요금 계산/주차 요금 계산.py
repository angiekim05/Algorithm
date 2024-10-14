from collections import defaultdict

def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    car_info = defaultdict(int)

    def to_minutes(x):
        hh,mm = map(int,x.split(":"))
        return hh*60+mm
    
    def calculate_fee(x):
        fee = base_fee
        if x > base_time:
            extra_time = x - base_time
            fee += extra_time // unit_time * unit_fee
            if extra_time % unit_time > 0:
                fee += unit_fee
        return fee

    for record in records:
        hhmm, car_numb, status = record.split()
        status = -1 if status == "IN" else 1
        car_info[car_numb] += to_minutes(hhmm) * status
    
    for k,v in sorted(car_info.items()):
        if v <= 0:
            v += to_minutes("23:59")
        answer.append(calculate_fee(v))

    return answer
