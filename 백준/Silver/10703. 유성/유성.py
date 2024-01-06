import sys
input = sys.stdin.readline
print = sys.stdout.write
n,m = map(int, input().split())
arr = [input() for _ in range(n)]
dist = 3001
for j in range(m):
    temp = -3001 # 만약 유성이 없으면
    for i in range(n):
        if arr[i][j] == "X":
            temp = i
        elif arr[i][j] == "#":
            dist = min(i-temp-1,dist)
            break

for i in range(min(n,dist)):
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
