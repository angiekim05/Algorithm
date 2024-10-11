import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
members = [[0] for _ in range(12)]
for i in range(n):
	p,w = map(int,input().split())
	heapq.heappush(members[p],-w)

for _ in range(k):
	for i in range(1,12):
		heapq.heappush(members[i],-max(0, -heapq.heappop(members[i]) - 1))
	
res = sum(-members[i][0] for i in range(1, 12))
			
print(res)