k = 1000000
n = int(input())
# 피사드 주기
m = 15*k//10
n %= m
f,s = 0,1
for i in range(n-1):
    f,s = s,(f+s)%k
print(s)