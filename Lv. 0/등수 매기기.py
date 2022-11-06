def solution(score):
    answer = []
    for i in range(len(score)):
        answer.append((score[i][0]+score[i][1])/2)
    
    tmp = []
    for j in answer:
        cnt = 1
        for k in answer:
            if j < k:
                cnt += 1
        tmp.append(cnt)
    return tmp
