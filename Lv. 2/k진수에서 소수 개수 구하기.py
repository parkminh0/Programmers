import math
def solution(n, k):
    tmp = ''
    while n != 0:
        tmp += str(n % k)
        n //= k
    tmp = tmp[::-1]
    
    answer = []
    tm = ''
    for i in range(len(tmp)):
        if tmp[i] != '0':
            tm += tmp[i]
        else:
            if tm != '':
                answer.append(int(tm))
                tm = ''
    if tm != '':
        answer.append(int(tm))
    
    cnt = 0
    for i in answer:
        sosu = True
        if i == 2:
            cnt += 1
            continue
        elif i % 2 == 0 or i == 1:
            continue
        else:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    sosu = False
                    break
        if sosu:
            cnt += 1
        
    return cnt