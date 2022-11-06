def solution(num_list, n):
    answer = []
    tmp = []
    for i in num_list:
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
        tmp.append(i)
    answer.append(tmp)
    return answer