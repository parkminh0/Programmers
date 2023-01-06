def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        test = True
        tmp = skill
        for j in i:
            if j in tmp:
                if tmp[0] != j:
                    test = False
                    break
                else:
                    tmp = tmp[1:]
            else:
                continue
        if test == True:
            answer += 1
            
    return answer