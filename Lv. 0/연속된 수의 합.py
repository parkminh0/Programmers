def solution(num, total):
    answer = []
    
    tmp = -50
    while total != int(num*(2*tmp+num-1)/2):
        tmp += 1
    
    for i in range(num):
        answer.append(tmp+i)
        
    return answer