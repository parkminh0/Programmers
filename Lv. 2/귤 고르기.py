def solution(k, tangerine):
    answer = 0
    a = list(set(tangerine))
    tmp = {}
    
    for i in a:
        tmp[i] = 0
    
    for j in tangerine:
        tmp[j] += 1

    tmp = sorted(tmp.values(), reverse = True)
    
    for l in tmp:
        k -= l
        answer += 1
        if k <= 0:
            return answer