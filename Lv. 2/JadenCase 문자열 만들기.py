def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if answer[-1] == ' ':
            answer += s[i].upper()
            continue
        else:
            answer += s[i].lower()
    return answer