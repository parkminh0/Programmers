def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) == 32:
            answer += i
        elif ord(i)+n > 122:
            answer += chr(ord(i)-26+n)
        elif ord(i) <= 90 and ord(i)+n > 90:
            answer += chr(ord(i)-26+n)
        else:
            answer += chr(ord(i)+n)
    return answer