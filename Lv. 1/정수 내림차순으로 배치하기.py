def solution(n):
    answer = ''
    tmp = []
    for i in str(n):
        tmp.append(i)
    
    tmp.sort(reverse=True)
    
    for j in tmp:
        answer += j
    return int(answer)