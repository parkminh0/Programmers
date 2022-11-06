def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        answer.append(1)
    
    idx = 0
    for i in emergency:
        for j in emergency:
            if i < j:
                answer[idx] += 1
        idx += 1
        
    return answer