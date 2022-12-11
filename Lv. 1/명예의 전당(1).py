def solution(k, score):
    answer = []
    tmp = []
    for i in score:
        answer.append(i)
        answer.sort()
        if len(answer) > k:
            answer.pop(0)
        tmp.append(answer[0])
    return tmp