def solution(s):
    for k in range(len(s),-1,-1):
        for i in range(len(s)-k+1):
            if s[i:i+k] == s[i:i+k][::-1]:
                return k