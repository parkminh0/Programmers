def solution(progresses, speeds):
    tmp = []
    for i in range(len(progresses)):
        x = (100-progresses[i])//speeds[i]
        if (100-progresses[i]) % speeds[i] != 0:
            x += 1
        tmp.append(x)
        
    ans = 1
    t = []
    idx = 0
    for j in range(1, len(tmp)):
        if tmp[idx] < tmp[j]:
            t.append(ans)
            idx = j
            ans = 1
        elif tmp[idx] >= tmp[j]:
            ans += 1
    t.append(ans)
        
    return t