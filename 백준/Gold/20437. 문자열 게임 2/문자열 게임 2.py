from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input() # 문자열
    k = int(input())
    ans = [10001,0] # 최소, 최대 길이

    # 문자열에서 문자별로 위치를 저장함
    words = defaultdict(list)
    for i in range(len(s)):
        words[s[i]].append(i)

    # 문자별로 k개 이상인 경우만 최소 혹은 최대 연속 문자열 길이를 구함
    for word in words.keys():
        n = len(words[word]) # 단어의 개수
        if len(words[word]) < k:
            continue
        for i in range(n-k+1): # 딱 k 개만 포함하는 문자열
            # 문자열의 길이
            temp = words[word][i+k-1]-words[word][i]+1
            if ans[0] > temp:
                ans[0] = temp
            if ans[1] < temp:
                ans[1] = temp

    if ans == [10001,0]: # 최소 최대가 변함이 없다면 답이 없다는 뜻임
        print(-1)
    else:
        print(*ans)