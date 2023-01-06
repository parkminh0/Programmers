def solution(lines):
    answer = 0
    tmp = []
    for i in lines:
        for j in range(i[0], i[1]):
            tmp.append(j)
            
    test = []
    for i in tmp:
        if tmp.count(i) > 1 and i not in test:
            answer += 1
            test.append(i)

    return answer