def solution(n, computers):
    def find(x):
        if x == networks[x]:
            return x
        networks[x] = find(networks[x])
        return networks[x]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x <= y:
            networks[y] = x
        else:
            networks[x] = y
        return

    networks = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]:
                union(i,j)

    nets = set()
    for i in range(n):
        nets.add(find(i))
    answer = len(nets)
    return answer