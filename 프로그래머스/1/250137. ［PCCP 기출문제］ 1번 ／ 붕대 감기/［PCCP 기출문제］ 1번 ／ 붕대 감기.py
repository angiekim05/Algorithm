def solution(bandage, health, attacks):
    bf = 0
    now = health
    for t,a in attacks:
        heal_time = t-bf-1
        heal = heal_time*bandage[1] + ((heal_time//bandage[0]) * bandage[2])
        now = min(health, now+heal)
        now -= a
        if now <= 0:
            return -1
        bf = t
    return now