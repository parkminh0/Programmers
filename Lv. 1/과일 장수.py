def solution(k, m, score):
    score.sort()
    
    s = 0
    while len(score) >= m:
        tmp = []
        for i in range(m):
            tmp.append(score.pop())
        s += min(tmp) * m

    return s