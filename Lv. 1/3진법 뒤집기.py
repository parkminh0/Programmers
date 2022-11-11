def solution(n):
    answer = 0
    
    tmp = []
    while n // 3 != 0:
        tmp.append(n % 3) 
        n = n // 3
    
    tmp.append(n)
    
    for i in range(len(tmp)):
        answer += tmp[i]*(3**(len(tmp)-i-1))
    return answer