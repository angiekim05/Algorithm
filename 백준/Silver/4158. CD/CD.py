import sys
input = sys.stdin.readline
n,m = map(int,input().split())
while n != 0 and m != 0:
    sang = set([int(input()) for _ in range(n)])
    sun = set([int(input()) for _ in range(n)])
    print(len(sang & sun))
    n,m = map(int,input().split())