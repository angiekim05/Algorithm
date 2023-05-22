import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in range(n):
    cnt = 0
    temp = float("inf")
    for j in range(i-1,-1,-1):
        a = (arr[i]-arr[j])/(i-j)
        if a < temp:
            cnt += 1
            temp = a
    temp = -float("inf")
    for j in range(i+1,n):
        a = (arr[i]-arr[j])/(i-j)
        if a > temp:
            cnt += 1
            temp = a
    ans = max(ans,cnt)
print(ans)