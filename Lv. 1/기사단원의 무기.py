def solution(number, limit, power):
    answer = 0
    tmp = []
    for i in range(1, number+1):
        cnt = 0
        for k in range(1, int(i**(1/2))+1):
            if i % k == 0:
                cnt += 1
                if k**2 != i:
                    cnt += 1
        tmp.append(cnt)

    for j in tmp:
        if j > limit:
            answer += power
        else:
            answer += j
    return answer