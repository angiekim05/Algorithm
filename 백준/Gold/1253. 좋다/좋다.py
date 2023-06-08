import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
if len(arr) < 3:
    print(0)
else:
    for tgt_idx in range(n):
        i = 0 if tgt_idx > 0 else 1
        j = n-1 if tgt_idx != n-1 else n-2
        s = arr[i] + arr[j]
        while i < j:
            if s == arr[tgt_idx]:
                ans += 1
                break
            elif s < arr[tgt_idx]:
                i += 1
                if i == tgt_idx:
                    i += 1
            else:
                j -= 1
                if j == tgt_idx:
                    j -= 1
            s = arr[i] + arr[j]
    print(ans)