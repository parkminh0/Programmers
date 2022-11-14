def solution(X, Y):
    answer = ''
    tmp = []

    for i in X:
        if i in Y:
            cnt = min(X.count(i), Y.count(i))
            for j in range(cnt):
                tmp.append(i)
            Y = Y.replace(i, "")
    if tmp == []:
        return '-1'

    tmp.sort(reverse = True)
    if tmp[0] == '0':
        return '0'
    
    for i in tmp:
        answer += i
    return answer
    