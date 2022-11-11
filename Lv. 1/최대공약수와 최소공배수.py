def solution(n, m):
    answer = []
    x = min(n, m)
    while True:
        if n % x == 0 and m % x == 0:
            answer.append(x)
            break
        x -= 1
    
    tmp = []
    y = 1
    while True:
        tmp.append(max(n,m)*y)
        if min(n,m) * y in tmp:
            answer.append(min(n, m)*y)
            break
        y += 1
    return answer