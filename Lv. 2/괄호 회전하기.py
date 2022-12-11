def solution(s):
    answer = 0
    tmp = ['()', '{}', '[]']
    for i in range(len(s)):
        s += s[0]
        s = s[1:]
        q = s
        for j in range(len(s)):
            if tmp[0] in q:
                q = q.replace(tmp[0], '')
            if tmp[1] in q:
                q = q.replace(tmp[1], '')
            if tmp[2] in q:
                q = q.replace(tmp[2], '')
        if q == '':
            answer += 1
    return answer