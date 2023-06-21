import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(1,n+1):
    ans.insert(i-arr[i-1]-1,i)
print(*ans)