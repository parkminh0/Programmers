def solution(numbers, target):
    answer = 0
    tmp = [[0]]
    for i in numbers:
        q = []
        x = tmp[-1]
        for j in x:
            q.append(j-i)
            q.append(j+i)
        tmp.append(q)

    return tmp[-1].count(target)