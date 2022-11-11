def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)