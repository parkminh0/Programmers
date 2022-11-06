def solution(spell, dic):
    for i in dic:
        count = 0
        for j in i:
            if i.count(j) >= 2:
                continue
            if j in spell:
                count += 1
        if count == len(i) and len(spell) == len(i):
            return 1
    return 2