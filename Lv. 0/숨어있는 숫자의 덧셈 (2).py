def solution(my_string):
    answer = 0
    tmp = 0
    for i in my_string:
        if i.isdigit() == True:
            tmp = tmp*10 + int(i)
        else:
            answer += tmp
            tmp = 0
    answer += tmp
    return answer