def solution(array):
    tmp = []
    for i in range(1000):
        tmp.append(array.count(i))
    if tmp.count(max(tmp)) >= 2:
        return -1
    else:
        return tmp.index(max(tmp))