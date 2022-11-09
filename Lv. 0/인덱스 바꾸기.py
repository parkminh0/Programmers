def solution(my_string, num1, num2):
    answer = ''
    tmp = []
    for i in my_string:
        tmp.append(i)
        
    a = tmp[num1]
    b = tmp[num2]
    tmp[num1] = b
    tmp[num2] = a
    for i in tmp:
        answer += i
    return answer