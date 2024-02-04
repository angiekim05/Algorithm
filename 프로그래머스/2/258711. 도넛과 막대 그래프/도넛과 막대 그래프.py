from collections import defaultdict
def solution(edges):
    answer = [0]*4
    g = defaultdict(list)
    inout = [defaultdict(int),defaultdict(int)]
    for a,b in edges:
        g[a].append(b)
        inout[0][b] += 1
        inout[1][a] += 1
    new = [x for x in inout[1].keys() if inout[0][x] == 0 and inout[1][x] > 1][0]
    answer[0] = new
    for start in g[new]:
        stack = [start]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                if stack:
                    answer[3]+=1
                else:
                    answer[1]+=1
                break
            visited.add(cur)
            for nx in g[cur]:
                stack.append(nx)
        else:
            answer[2] += 1
    return answer