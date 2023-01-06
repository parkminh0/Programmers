def solution(num, total):
    answer = []
    
    start = -50
    while True:
        test = start
        for i in range(1, num):
            test += start + i
            
        if test == total:
            break
            
        start += 1
    
    for i in range(num):
        answer.append(start+i)
        
    return answer