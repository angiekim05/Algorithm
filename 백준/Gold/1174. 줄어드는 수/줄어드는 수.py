from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

q = deque(list(range(10)))
idx = 0
while q:
    x = q.popleft()
    idx += 1
    if idx == n:
        print(x)
        break

    for nx in range(x % 10):
        q.append(x*10+nx)
else:
    print(-1)