def solution(ingredient):
    answer = 0
    tmp = []
    for i in ingredient:
        tmp.append(i)
        if len(tmp) >= 4 and tmp[-1] == 1 and tmp[-2] == 3 and tmp[-3] == 2 and tmp[-4] == 1:
            answer += 1
            for i in range(4):
                tmp.pop()
    return answer