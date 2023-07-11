import sys
input = sys.stdin.readline
t = int(input())
paper = [list(map(int, input().rstrip().split())) for _ in range(t)]
n1, n0 = 0, 0


def check(sqr):
    flag = 0
    for i in range(len(sqr)):
        if len(set(sqr[i])) != 1:
            return -1
        else:
            flag += sqr[i][0]
    if flag == 0:
        return 0
    elif flag == len(sqr):
        return 1
    else:
        return -1


def quarter(sqr):
    global n1
    global n0
    k = check(sqr)
    if k == 0:
        n0 += 1
    elif k == 1:
        n1 += 1
    elif k == -1:
        a, b, c, d = [], [], [], []
        for i in range(len(sqr)):
            mid = len(sqr) // 2
            if i < mid:
                a.append(sqr[i][:mid])
                b.append(sqr[i][mid:])
            else:
                c.append(sqr[i][:mid])
                d.append(sqr[i][mid:])
        quarter(a)
        quarter(b)
        quarter(c)
        quarter(d)


quarter(paper)
print(n0, n1, sep="\n")

