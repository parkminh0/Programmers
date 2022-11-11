def solution(answers):
    answer = []
    x = [1, 2, 3, 4, 5] * len(answers)
    y = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    
    answer = [0, 0, 0]
    for i in range(len(answers)):
        if x[i] == answers[i]:
            answer[0] += 1
        if y[i] == answers[i]:
            answer[1] += 1
        if z[i] == answers[i]:
            answer[2] += 1
    
    qq = max(answer)
    tmp = []
    if answer[0] == qq:
        tmp.append(1)
    if answer[1] == qq:
        tmp.append(2)
    if answer[2] == qq:
        tmp.append(3)
    return tmp