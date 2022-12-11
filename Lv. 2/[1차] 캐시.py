def solution(cacheSize, cities):
    answer = 0
    tmp = []

    if cacheSize == 0:
        return len(cities) * 5
    
    while cities:
        if cities[0].upper() in tmp:
            tmp.pop(tmp.index(cities[0].upper()))
            answer += 1
        else:
            answer += 5
        tmp.append(cities.pop(0).upper())
        if len(tmp) == cacheSize + 1:
            tmp.pop(0)
            
    return answer