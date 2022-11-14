def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        s = ''
        tmp = ''
        for j in i:
            s += j
            if s in baby:
                if s == tmp[-len(s):]:
                    break
                tmp += s
                s = ''
        if s == '':
            answer += 1
    return answer