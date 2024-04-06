import heapq
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
jewels.sort(key = lambda x: (-x[0],x[1]))
bags = [int(input()) for _ in range(k)]
bags.sort()

q = []
answer = 0
for b in bags:
    while jewels and b >= jewels[-1][0]:
        w,v = jewels.pop()
        heapq.heappush(q,-v)
    if q:
        answer += -heapq.heappop(q)
print(answer)