from bisect import bisect_left
from itertools import combinations
import heapq
def summation(dice,case,n):
    s = []
    def sol(cnt,x):
        if cnt == n//2:
            s.append(x)
            return
        for i in range(6):
            sol(cnt+1,x+dice[case[cnt]-1][i])
    sol(0,0)
    s.sort()
    return s

def winner(case, countercase):
    win = 0
    for x in case:
            win += bisect_left(countercase, x)
    return win

def solution(dice):
    answer = []
    m = 0
    n = len(dice)
    comb = list(combinations(list(range(1,1+n)),n//2))
    for case in comb[:len(comb)//2]:
        countercase = sorted(set(list(range(1,1+n))) - set(list(case)))
        a = summation(dice,case,n)
        b = summation(dice,countercase,n)
        w = winner(a, b)
        w2 = winner(b, a)
        heapq.heappush(answer,(-w,list(case)))
        heapq.heappush(answer,(-w2,countercase))
    return answer[0][1]