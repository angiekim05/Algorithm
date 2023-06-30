import sys
input = sys.stdin.readline

s, N, K, R1, R2, C1, C2 = map(int, input().split())

def check(l, x, y):
    if l == 1:
        return 0
    block = l // N
    if block * (N - K) // 2 <= x < block * (N + K) // 2 and block * (N - K) // 2 <= y < block * (N + K) // 2:
        return 1
    return check(block,x%block,y%block)

for i in range(R1,R2+1):
    for j in range(C1,C2+1):
        print(check(N ** s,i,j),end="")
    print()