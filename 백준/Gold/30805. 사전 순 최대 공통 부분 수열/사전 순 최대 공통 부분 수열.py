import sys
input = sys.stdin.readline
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

arr = set(arrA)&set(arrB)
if not arr:
    print(0)
    exit()

ans = []
while arr:
    x = max(arr)
    ans.append(x)
    idx1 = arrA.index(x)
    idx2 = arrB.index(x)
    arrA = arrA[idx1+1:]
    arrB = arrB[idx2+1:]
    arr = set(arrA) & set(arrB)

print(len(ans))
print(*ans)