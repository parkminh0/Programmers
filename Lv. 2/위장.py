def solution(clothes): 
    tmp = []
    for i in clothes:
        tmp.append(i[1])
    
    x = []
    answer = []
    for j in tmp:
        inp = [j, tmp.count(j)]
        if inp in x:
            continue
        x.append([j, tmp.count(j)])
        answer.append(inp[1])
        
    result = 1
    for i in answer:
        result *= (i+1)
        
    return result-1