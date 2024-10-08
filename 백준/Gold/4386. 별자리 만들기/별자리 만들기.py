import sys
input = sys.stdin.readline

def dist(a,b):
    ax,ay = a
    bx,by = b
    return round(((ax-bx)**2+(ay-by)**2)**0.5, 2)
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
nodes = []
edges = []
parent = list(range(n))
res = 0
for i in range(n):
    nodes.append(list(map(float,input().split())))
    for j in range(i):
        d = dist(nodes[i],nodes[j])
        edges.append((d,i,j))
edges.sort(key = lambda x: x[0])
for i in range(len(edges)):
    d,x,y = edges[i]
    if find(x) != find(y):
        union(x,y)
        res += d
print(res)