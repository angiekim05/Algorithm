import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n + m == 0:
        break
    sang = set([int(input()) for _ in range(n)])
    ans = 0
    for _ in range(m):
        if int(input()) in sang:
            ans += 1
    print(ans)