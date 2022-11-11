def solution(s):
    string = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    tmp = ''
    
    for i in s:
        if i.isdigit() == True:
            answer += i
        else:
            tmp += i
            if tmp in string:
                answer += str(string.index(tmp))
                tmp = ''
                
    return int(answer)