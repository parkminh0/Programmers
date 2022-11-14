def solution(survey, choices):
    answer = ''
    type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    val = [0]*8
    choice = [0, 3, 2, 1, 0, 1, 2, 3]
    
    for i in range(len(survey)):
        if choices[i] < 4:
            val[type.index(survey[i][0])] += choice[choices[i]]
        elif choices[i] > 4:
            val[type.index(survey[i][1])] += choice[choices[i]]

    for j in range(0, 8, 2):
        if val[j] >= val[j+1]:
            answer += type[j]
        elif val[j] < val[j+1]:
            answer += type[j+1]
    return answer