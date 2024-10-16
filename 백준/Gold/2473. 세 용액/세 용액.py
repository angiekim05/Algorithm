import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 정렬하기
closeZero = float("INF") # 0과 가장 가까운 합을 저장해 놓을 변수
res = []   # 최고의 조합을 담을 리스트

for k in range(n-2): # 임의의 용액을 고정
    left, right = k+1, n-1 # 선택된 용액 이후의 최소값 최대값 위치

    while left < right < n:
        curSum = arr[k] + arr[left] + arr[right]

        # 현재 합이 0에 더 가까운 경우 업데이트
        if abs(curSum) < abs(closeZero):
            closeZero = abs(curSum)
            res = [arr[k], arr[left], arr[right]]

        # 0이면 최고의 조합임으로 탐색 종료
        if curSum == 0:
            print(*res)
            exit()
        elif curSum > 0: # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
            right -= 1
        else: # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
            left += 1

print(*res)