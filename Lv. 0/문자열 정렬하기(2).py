def solution(my_string):
    answer = ''
    tmp = my_string.lower()
    ref = []
    for i in tmp:
        ref.append(i)

    ref.sort()
    for i in ref:
        answer += i
        
    return answer