import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m,k = map(int, input().split())
    houses = list(map(int, input().split()))
    
    if n == m:
        if sum(houses) < k:
            print(1)
        else:
            print(0)
        continue
    
    houses += houses
    ans = 0
    cur = sum(houses[:m])
    for i in range(n):
        if cur < k:
            ans += 1
        cur -= houses[i]
        cur += houses[i+m]

    print(ans)