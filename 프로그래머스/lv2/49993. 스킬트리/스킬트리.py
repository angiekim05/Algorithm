def solution(skill, skill_trees):
    answer = 0
    start = skill[0]
    skill = {skill[i]:skill[i-1] for i in range(len(skill)-1,0,-1)}
    for s in skill_trees:
        temp = set()
        for x in s:
            if x in skill and skill[x] not in temp:
                break
            temp.add(x)
        else:
            answer += 1
    return answer