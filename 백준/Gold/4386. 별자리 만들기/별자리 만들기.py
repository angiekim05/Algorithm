import sys
input = sys.stdin.readline

n = int(input())
nodes = [list(map(float,input().split())) for _ in range(n)]

def dist(a,b):
    ax,ay = a
    bx,by = b
    return round(((ax-bx)**2+(ay-by)**2)**0.5, 2)

edges = []
for i in range(n):
    for j in range(i+1,n):
        d = dist(nodes[i],nodes[j])
        edges.append((d,i,j))
parent = list(range(n+1))
res = 0

# 간선을 최소 비용 순으로 오름차순 정렬
edges.sort(key = lambda x: x[0])

# Union-Find 알고리즘
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

for i in range(len(edges)):
    d,x,y = edges[i]
    if find(x) != find(y):
        union(x,y) # 최소 신장트리에 포함시킴
        res += d

print(res)