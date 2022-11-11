def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 1
        count = 0
        while cnt <= i:
            if i % cnt == 0:
                count += 1
            cnt += 1
            
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer