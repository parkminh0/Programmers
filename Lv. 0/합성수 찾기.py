def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        div = 1
        while div <= i:
            if i % div == 0:
                cnt += 1
                if cnt == 3:
                    answer += 1
                    break
            div += 1
    return answer