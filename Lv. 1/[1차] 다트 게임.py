def solution(dartResult):
    answer = []
    q = [0, 'S', 'D', 'T']
    x = ''
    for i in dartResult:
        if i.isdigit() == True:
            x += i
        elif i in q:
            answer.append(int(x)**q.index(i))
            x = ''
        elif i == '*':
            if len(answer) == 3:
                answer[1] *= 2
                answer[2] *= 2
            else:
                for j in range(len(answer)):
                    answer[j] *= 2
        elif i == '#':
            answer[-1] *= -1
    return sum(answer)