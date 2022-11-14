def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i]//2)
    
    answer += '0'
    
    for i in reversed(answer):
        if i == '0':
            continue
        answer += i
    return answer