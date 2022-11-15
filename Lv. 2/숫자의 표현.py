def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        cnt = i+1
        while i <= n:
            if i == n:
                answer += 1
                break
            i += cnt
            cnt += 1
            
            
    return answer