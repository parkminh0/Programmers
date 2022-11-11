def solution(n):
    answer = 0
    while answer**2 <= n:
        if answer**2 == n:
            return (answer+1)**2
        answer += 1
    return -1