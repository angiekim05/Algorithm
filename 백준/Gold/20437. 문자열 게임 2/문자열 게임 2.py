from collections import defaultdict
import sys
input = sys.stdin.readline

def sol():
    s = input() # 문자열
    k = int(input())
    ans = [] # 문자열의 길이를 담을 리스트

    # 문자열에서 문자별로 위치를 저장함
    words = defaultdict(list)
    for i in range(len(s)):
        words[s[i]].append(i)

    # 문자별로 k개 이상인 경우만 최소 혹은 최대 연속 문자열 길이를 구함
    for word in words.values():
        n = len(word) # 단어의 개수
        if n < k:
            continue
        for i in range(n-k+1): # 딱 k 개만 포함하는 문자열
            # 문자열의 길이
            temp = word[i+k-1] - word[i] + 1
            ans.append(temp)

    if ans: # 최소 최대가 변함이 없다면 답이 없다는 뜻임
        print(min(ans),max(ans))
    else:
        print(-1)

t = int(input())
for _ in range(t):
    sol()