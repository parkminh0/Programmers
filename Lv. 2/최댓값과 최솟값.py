def solution(s):
    answer = []
    tmp = s.split(" ")
    for i in tmp:
        answer.append(int(i))
    
    result = ' '
    return str(min(answer)) + result + str(max(answer))