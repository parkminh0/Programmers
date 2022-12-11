import math
def solution(fees, records):
    inf = []
    for i in records:
        inf.append(i.split(" "))
    inf = sorted(inf, key = lambda x : x[1])
    tmp = []
    answer = []
    
    for i in inf:
        x = i[0].split(':')
        time = 1439 - (int(x[0])*60+int(x[1]))
        if i[2] == 'IN':
            if i[1] in tmp:
                answer[-1] += time
            elif i[1] not in tmp:
                tmp.append(i[1])
                answer.append(time)
        else:
            answer[-1] -= time        
    
    ans = []
    for j in answer:
        if j <= fees[0]:
            ans.append(fees[1])
        else:
            ans.append(fees[1] + math.ceil((j-fees[0])/fees[2])*fees[3])
    return ans