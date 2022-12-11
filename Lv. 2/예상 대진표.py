def solution(n,a,b):
    tmp = []
    for i in range(n-2):
        tmp.append('')

    if a >= b:
        tmp.insert(b-1, 'B')
        tmp.insert(a-1, 'A')
    else:
        tmp.insert(a-1, 'A')
        tmp.insert(b-1, 'B')
    
    answer = 1
    while True:
        x = []
        for i in range(0, len(tmp), 2):
            if tmp[i] + tmp[i+1] == 'AB' or tmp[i] + tmp[i+1] == 'BA':
                return answer
                break
            x.append(tmp[i]+tmp[i+1])
        answer += 1
        tmp = x