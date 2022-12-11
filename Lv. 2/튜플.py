def solution(s):
    tmp = s[2:-2].split("},{")
    answer = []
    q = []
    for i in range(len(tmp)):
        q.append([len(tmp[i]), tmp[i]])
    
    q = sorted(q, key = lambda x : x[0])

    for i in q:
        x = i[1].split(',')
        for j in x:
            if int(j) not in answer:
                answer.append(int(j))
            
    return answer