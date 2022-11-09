def solution(my_string):
    answer = ''
    
    for i in my_string:
        x = i.upper()
        y = i.lower()
        if i == x:
            answer += y
        else:
            answer += x
            
    return answer