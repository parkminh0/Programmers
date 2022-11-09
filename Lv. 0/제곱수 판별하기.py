def solution(n):
    for i in range(int(n/2)+1):
        if i**2 == n:
            return 1
    return 2