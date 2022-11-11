def solution(s):
    tmp = []
    for i in s:
        tmp.append(i)
    tmp.sort(reverse = True)
    
    answer = ''
    for j in tmp:
        answer += j
    return answer