def solution(record):
    answer = []
    result = []
    dic = {}
    for i in record:
        i = i.split(" ")
        answer.append(i)
        
    for j in answer:
        if len(j) == 2:
            continue
        dic[j[1]] = j[2]
    
    for k in answer:
        if k[0] == 'Enter':
            result.append(str(dic[k[1]])+'님이 들어왔습니다.')
        elif k[0] == 'Leave':
            result.append(str(dic[k[1]]+'님이 나갔습니다.'))
            
    return result