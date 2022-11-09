def solution(array, n):
    array.sort()
    answer = []
    for i in array:
        answer.append(abs(i-n))

    idx = answer.index(min(answer))
    
    return array[idx]