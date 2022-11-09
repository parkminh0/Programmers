def solution(babbling):
    answer = 0
    tmp = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        test = ''
        for j in i:
            test += j
            if test in tmp:
                test = ''
        if test == '':
            answer += 1
    
    return answer