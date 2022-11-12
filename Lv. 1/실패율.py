def solution(N, stages):
    answer = []
    stage = 1
    y = len(stages)
    while stage <= N:
        x = stages.count(stage)
        if y == 0:
            answer.append([stage, 0])
        else:
            answer.append([stage, x/y])
        y -= x
        stage += 1
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    
    result = []
    for i in answer:
        result.append(i[0])
        
    return result