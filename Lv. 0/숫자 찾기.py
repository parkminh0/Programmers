def solution(num, k):
    answer = 0
    for i in str(num):
        answer += 1
        if str(k) == i:
            return answer
    return -1