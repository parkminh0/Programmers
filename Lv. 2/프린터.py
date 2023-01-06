def solution(priorities, location):
    answer = 1
    tmp = []
    for i in range(len(priorities)):
        tmp.append([priorities[i], i])
    
    while True:
        idx = tmp.index(max(tmp, key = lambda x : x[0]))
        tmp = tmp[idx:] + tmp[:idx]
        if location == tmp[0][1]:
            return answer
        else:
            del tmp[0]
            answer += 1
            
    return answer