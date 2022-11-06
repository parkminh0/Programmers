def solution(s):
    answer = s.split(" ")
    tmp = []
    for i in answer:
        if i == 'Z':
            tmp.pop(-1)
        else:
            tmp.append(int(i))
            
    return sum(tmp)