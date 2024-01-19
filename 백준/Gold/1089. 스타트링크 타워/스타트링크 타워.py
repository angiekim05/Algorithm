import sys
input = sys.stdin.readline
n = int(input())

can_make = {(0,0):{0,2,3,4,5,6,7,8,9},
            (0,1):{0,2,3,5,6,7,8,9},
            (0,2):{0,1,2,3,4,5,6,7,8,9},
            (1,0):{0,4,5,6,8,9},
            (1,1):set(),
            (1,2):{0,1,2,3,4,7,8,9},
            (2,0):{0,2,3,4,5,6,8,9},
            (2,1):{2,3,4,5,6,8,9},
            (2,2):{0,1,2,3,4,5,6,7,8,9},
            (3,0):{0,2,6,8},
            (3,1):set(),
            (3,2):{0,1,3,4,5,6,7,8,9},
            (4,0):{0,2,3,5,6,8,9},
            (4,1):{0,2,3,5,6,8,9},
            (4,2):{0,1,2,3,4,5,6,7,8,9}}


numb = [input() for _ in range(5)]
res = 0.0
for s in range(n):
    can_ = set(range(10))
    for i in range(5):
        for j in range(s*4,s*4+3):
            if numb[i][j] == "#":
                can_ &= can_make[(i,j%4)]
    if can_:
        res *= 10
        res += sum(can_)/len(can_)
    else:
        res = -1
        break

print(res)