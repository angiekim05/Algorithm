import sys
input = sys.stdin.readline
print = sys.stdout.write
n,m = map(int, input().split())
arr = [input() for _ in range(n)]

def get_dist():
    dist = n
    for j in range(m):
        temp = -3001 # 만약 유성이 없으면
        for i in range(n):
            if arr[i][j] == "X":
                temp = i
            elif arr[i][j] == "#":
                dist = min(i-temp-1,dist)
                break
    return dist

def restore():
    dist = get_dist()
    for i in range(dist):
        res = ""
        for j in range(m):
            if arr[i][j] == "#":
                res += "#"
            else:
                res += "."
        print(res+"\n")

    for i in range(dist, n):
        res = ""
        for j in range(m):
            if arr[i-dist][j] == "X":
                res += "X"
            elif arr[i][j] == "#":
                res += "#"
            else:
                res += "."
        print(res+"\n")

restore()