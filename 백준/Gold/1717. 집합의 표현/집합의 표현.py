import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n,m = map(int,input().split())

group = list(range(n+1))

def find(x):
    if group[x] == x:
        return x
    group[x] = find(group[x])
    return group[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x <= y:
        group[y] = x
    else:
        group[x] = y

for _ in range(m):
    p,a,b = map(int,input().split())
    if p == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
