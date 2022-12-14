def solution(s):
    answer = 0
    tmp = ''
    x = 0
    y = 0
    for i in s:
        if tmp == '':
            tmp += i
            x += 1
        else:
            if tmp[0] == i:
                x += 1
            elif tmp[0] != i:
                y += 1
            if x == y:
                answer += 1
                tmp = ''
    if tmp != '':
        answer += 1
    return answer