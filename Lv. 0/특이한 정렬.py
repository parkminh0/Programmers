def solution(numlist, n):
    answer = []
    tmp = []
    for i in range(len(numlist)):
        answer.append([abs(numlist[i]-n), i])
    answer.sort()
    if len(numlist) == 1:
        return numlist
    for k in range(len(answer)-1):
        if answer[k][0] == answer[k+1][0]:
            a = answer[k][1]
            b = answer[k+1][1]
            if numlist[answer[k][1]] < numlist[answer[k+1][1]]:
                answer[k+1][1] = a
                answer[k][1] = b
    for i in range(len(numlist)):
        tmp.append(numlist[answer[i][1]])
    return tmp