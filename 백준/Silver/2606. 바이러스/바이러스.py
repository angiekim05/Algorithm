import sys

input = sys.stdin.readline
node_n = int(input())
link_n = int(input())
root = [i for i in range(node_n + 1)]
root[1] = 1


def find_root(n):
    if n == root[n]:
        return n
    temp = root[n]
    new = find_root(temp)
    root[n] = new
    return new


def link(a, b):
    A = find_root(a)
    B = find_root(b)

    if A < B:
        root[B] = A
    else:
        root[A] = B


for i in range(link_n):
    a, b = map(int, input().rstrip().split())
    link(a, b)
cnt = -1
for i in range(node_n + 1):
    if find_root(i) == 1:
        cnt += 1
print(cnt)
