def solution(msg):
    answer = []
    tmp = ['', 'A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    x = ''
    for i in msg:
        x += i
        print(x)
        if x not in tmp:
            tmp.append(x)
            answer.append(tmp.index(x[:-1]))
            x = i
    answer.append(tmp.index(x))
    return answer