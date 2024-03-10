import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    answer = [[],[]]

    def sol(l):
        if len(l) == 1:
            answer[0].append(l[0][2])
            answer[1].append(l[0][2])
            return
        maxy, idx = 0,0
        for i in range(len(l)):
            if maxy < l[i][1]:
                maxy = l[i][1]
                idx = i
        answer[0].append(l[idx][2])
        left = l[:idx]
        right = l[idx+1:]
        if left:
            sol(left)
        if right:
            sol(right)
        answer[1].append(l[idx][2])

    nodeinfo = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]
    nodeinfo.sort()
    sol(nodeinfo)

    return answer