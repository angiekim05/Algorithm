import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 총 집 개수, 연속으로 훔질 집 개수, 자동 방범 장치 작동 최소 비용
    n,m,k = map(int, input().split())
    # 돈의 양
    houses = list(map(int, input().split()))
    
    if n == m:
        if sum(houses) < k:
            ans = 1
        else:
            ans = 0
    else:
        houses += houses
        ans = 0
        cur = sum(houses[:m])
        for i in range(n):
            if cur < k:
                ans += 1
            cur -= houses[i]
            cur += houses[i+m]

    print(ans)