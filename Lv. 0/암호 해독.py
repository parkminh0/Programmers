def solution(cipher, code):
    answer = ''
    cnt = 1
    for i in cipher:
        if cnt % code == 0:
            answer += i
        cnt += 1
    return answer