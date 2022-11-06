def solution(n):
    answer = 1
    tmp = 1
    while answer <= n:
        answer *= tmp
        tmp += 1
    return tmp-2