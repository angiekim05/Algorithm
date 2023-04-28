def solution(n, words):
    # 탈락하는 사람의 번호, 자신의 몇 번째 차례에 탈락하는지
    words += [words[-1][-1]+words[0][0]]
    answer = [0,0]
    used = set()
    for turn in range(1,101):
        for i in range(1,n+1):
            idx = (turn-1) * n + i - 1
            if idx + 1 > len(words):
                return [0,0]
            w = words[idx]
            if w in used or w[0] != words[idx-1][-1]:
                return [i,turn]
            used.add(w)