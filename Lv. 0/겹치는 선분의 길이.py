def solution(lines):
    tmp = []
    for i in lines:
        q = []
        for j in range(i[0], i[1]+1):
            q.append(j)
        tmp.append(q)

    test = []
    for j in range(len(tmp)-1):
        q = []
        for k in tmp[j]:
            if k in tmp[j+1]:
                q.append(k)
        test.append(q)
    q = []
    for i in tmp[0]:
        if i in tmp[2]:
            q.append(i)
    test.append(q)

    tmp = []    
    for i in test:
        if len(i) > 1:
            for j in i:
                if j != tmp:
                    tmp.append(j)
                
    tmp.sort()
    cnt = 0
    for i in range(len(tmp)-1):
        if tmp[i] + 1 == tmp[i+1]:
            cnt += 1
    return cnt