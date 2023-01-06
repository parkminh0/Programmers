def solution(n, t, m, p):
    answer = ''
    tmp = ''
    num = [10, 11, 12, 13, 14, 15]
    alp = ['A', 'B', 'C', 'D', 'E', 'F']
    
    k = 0
    while len(answer) < t*m:
        i = k
        if i >= n:
            while i >= n :
                if i % n >= 10:
                    tmp += alp[(i % n) - 10]
                else:
                    tmp += str(i % n)
                i = i // n
            if i >= 10:
                tmp += alp[(i % n) - 10]
            else:
                tmp += str(i)
        else:
            if i >= 10:
                tmp += alp[(i % n) - 10]
            else:
                tmp += str(i)
        answer += tmp[::-1]
        k += 1
        tmp = ''

    result = ''
    for j in range(p-1, len(answer), m):
        result += answer[j]
        if len(result) == t:
            return result