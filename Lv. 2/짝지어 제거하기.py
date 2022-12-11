def solution(s):
    tmp = ['0']
    for i in s:
        if tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)
    
    if tmp == ['0']:
        return 1
    else:
        return 0