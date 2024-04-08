import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
gems = defaultdict(list)
for _ in range(n):
    m,v = map(int, input().split())
    gems[m].append(v)
# 보석의 최대 무게가 1000000라서 더 큰 가방을 볼 필요 없음
bags = [min(1000000,int(input())) for _ in range(k)]
gems_w = sorted(gems.keys(),reverse=True)
bags.sort()
pq = []
for w in gems_w:
    for v in gems[w]:
        if bags and bags[-1] >= w:
            bags.pop()
            heapq.heappush(pq,v)
        elif pq and v > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq,v)
print(sum(pq))