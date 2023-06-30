import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

cur = deque([(n, 0)])
visited = [0] * (200000)
min_time = float("inf")
while cur:
    x, t = cur.popleft()
    if x == k:
        min_time = min(min_time, t)

    if x > k:
        min_time = min(min_time, t + (x - k))

    if x < k:
        # 순간이동
        next_x = x * 2
        if 0 <= next_x <= 100000 and not visited[next_x]:
            visited[next_x] = 1
            cur.appendleft((next_x, t))
        # 뒤로 걷기
        next_x = x - 1
        if 0 <= next_x <= 100000 and not visited[next_x]:
            visited[next_x] = 1
            cur.append((next_x, t + 1))
        # 앞으로 걷기
        next_x = x + 1
        if 0 <= next_x <= 100000 and not visited[next_x]:
            visited[next_x] = 1
            cur.append((next_x, t + 1))
        
print(min_time)
