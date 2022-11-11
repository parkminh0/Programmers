import math
def solution(n):
    answer = 1
    num = [2]
    for i in range(2, n+1):
        if i % 2 == 0:
            continue
        sosu = True
        for j in num:
            if math.sqrt(i) >= j:
                if i % j == 0:
                    sosu = False
                    break
            else:
                break
        if sosu == True:
            num.append(i)
            answer += 1
    return answer