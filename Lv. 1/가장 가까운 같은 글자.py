def solution(s):
    answer = []
    tmp = []
    for i in s:
        if i not in tmp:
            answer.append(-1)
            tmp.append(i)
        else:
            answer.append(len(answer) - tmp.index(i))
            tmp[tmp.index(i)] = 0
            tmp.append(i)
    return answer