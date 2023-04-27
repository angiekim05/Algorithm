from collections import defaultdict
import sys
input = sys.stdin.readline

# 쿼리 개수
n = int(input())

# 고릴라 정보상
go = defaultdict(list)

# 호석이가 얻는 정보 가치
ans = 0

for i in range(n):
    s = input().split()
    if s[0] == "1": # 고릴라 정보상이 갖는 정보
        # 가치 정보를 정수로 바꾸어 리스트에 추가
        go[s[1]].extend(list(map(int,s[3:])))
        # 리스트 정렬
        go[s[1]].sort()
        
    # 호석이가 정보를 사감
    else:
        # 호석이가 사갈 수 있는 정보의 개수
        k = min(len(go[s[1]]),int(s[2]))
        for _ in range(k):
            ans += go[s[1]].pop()

print(ans)