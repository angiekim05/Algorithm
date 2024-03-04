from collections import deque
def solution(begin, target, words):
    if target not in set(words):
        return 0
    n = len(words)
    m = len(words[0])
    g = [[] for _ in range(n+1)]
    words.append(begin)
    for i in range(n+1):
        w1 = words[i-1]
        for j in range(1,n+1):
            if i == j:
                continue
            w2 = words[j-1]
            cnt = 0
            for k in range(m):
                if w1[k] == w2[k]:
                    cnt += 1
            if m-cnt == 1:
                g[i].append(j)
    
    q = deque([(0,0)])
    visited = [0]*(n+1)
    visited[0] = 1
    while q:
        cur, cnt = q.popleft()
        if words[cur-1] == target:
            return cnt
        for nx in g[cur]:
            if not visited[nx]:
                visited[nx] = 1
                q.append((nx,cnt+1))
    return cnt