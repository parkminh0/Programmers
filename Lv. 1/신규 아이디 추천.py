def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    lv2 = ['-', '_', '.']
    for i in new_id:
        if ord(i) <= 122 and ord(i) >= 97:
            answer += i
        if i.isdigit() == True:
            answer += i
        if i in lv2:
            if i == '.' and answer == '':
                continue
            if i == '.' and answer[-1] == '.':
                continue
            answer += i
    if answer == '':
        answer += 'a'
    elif answer[-1] == '.':
        while answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) >= 16: 
        answer = answer[:15]
        if answer[-1] == '.':
            while answer[-1] == '.':
                answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    return answer