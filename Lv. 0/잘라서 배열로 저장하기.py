def solution(my_str, n):
    answer = []
    tmp = ''
    for i in my_str:
        tmp += i
        if len(tmp) == n:
            answer.append(tmp)
            tmp = ''
    if tmp != '':
        answer.append(tmp)
    return answer