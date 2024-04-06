import heapq
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort(reverse=True)
bags.sort()
pq = []
answer = 0
for x in bags:
    while gems:
        if gems[-1][0] > x:
            break
        nm,nv = gems.pop()
        heapq.heappush(pq,-nv)
    if pq:
        answer -= heapq.heappop(pq)
print(answer)