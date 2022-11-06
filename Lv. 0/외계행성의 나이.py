def solution(age):
    result = ''
    for i in str(age):
        result += chr(97+int(i))
    return result