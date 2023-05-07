import sys
input = sys.stdin.readline

# 순서가 바뀔 수 있음
i,j = sorted(map(int,input().split()))
x,y = map(int,input().split())

# 범위 밖으로 넘어가는 경우도 Unknwon
if 0 <= y < abs(x):
    cnt = 0 # 딱 한번만 나와야 함
    q = (i//abs(x)-1)*abs(x)+y # 시작 위치는 i이하부터
    while q <= j:
        if i <= q <= j: # 범위 안에 들어오는 값이 있다면 cnt 증가
            cnt += 1
        if cnt > 1: # 2개 이상 가능하다면 Unknwon
            break
        q += abs(x) # |x|만큼 증가시킴

    if cnt == 1:
        print(q-abs(x))
    else:
        print("Unknwon Number")
else:
    print("Unknwon Number")