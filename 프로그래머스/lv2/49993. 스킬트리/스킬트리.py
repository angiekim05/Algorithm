def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        can_do = True
        for i in range(len(skill_tree)):
            idx = skill.find(skill_tree[i])
            if idx <= 0:
                continue
            for s in skill[:idx]:
                if s not in skill_tree[:i]:
                    can_do = False
                    break
            if not can_do:
                break
        else:
            ans += 1
    return ans