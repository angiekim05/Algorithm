import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
z = float("INF")
zarr = []
for k in range(n-2):
    i,j = k+1, n-1
    x = arr[k] + arr[i] + arr[j]
    z_ = abs(x)
    while i < j < n:
        if z > z_:
            z = z_
            zarr = [arr[k], arr[i], arr[j]]
        if x > 0:
            j -= 1
            x += arr[j] - arr[j+1]
        else:
            i += 1
            x += arr[i] - arr[i-1]
        z_ = abs(x)


print(*zarr)