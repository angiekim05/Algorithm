import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for tgt_idx in range(n):
    i = 0
    j = n-1
    while i < j:
        s = arr[i] + arr[j]
        if s == arr[tgt_idx]:
            if i == tgt_idx:
                i += 1
            elif j == tgt_idx:
                j -= 1
            else:
                ans += 1
                break
        elif s < arr[tgt_idx]:
            i += 1
        else:
            j -= 1
print(ans)