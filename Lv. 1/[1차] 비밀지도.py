def solution(n, arr1, arr2):
    q = []
    p = []
    for i in range(n):
        x = str(bin(arr1[i]))[2:]
        y = str(bin(arr2[i]))[2:]
        if len(x) < n:
            for j in range(n-len(x)):
                x = '0' + x
        if len(y) < n:
            for k in range(n-len(y)):
                y = '0' + y
        q.append(x)
        p.append(y)
        
    answer = []
    for i in range(len(q)):
        tmp = ''
        for j in range(len(q)):
            if q[i][j] == '1' or p[i][j]  == '1':
                tmp += '#'
            elif q[i][j] == '0' and p[i][j] == '0':
                tmp += " "
        answer.append(tmp)
    return answer