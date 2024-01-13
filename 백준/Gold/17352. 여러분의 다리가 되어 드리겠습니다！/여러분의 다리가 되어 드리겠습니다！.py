n = int(input())
parents = list(range(n+1))
parents[0] = 1

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for _ in range(n-2):
    s,e = map(int,input().split())
    union(s,e)
for i in range(n):
    find(i)
res = list(set(parents))
print(res[0],res[1])