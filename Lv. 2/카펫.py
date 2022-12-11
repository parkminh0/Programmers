def solution(brown, yellow):
    x = 3
    y = 3
    while True:
        tmp = x
        if (x-2)*(y-2) == yellow and x*y - yellow == brown:
                return [x, y]
        while tmp <= brown:
            if (tmp-2)*(y-2) == yellow and tmp*y - yellow == brown:
                return [tmp, y]
            tmp += 1
        x += 1
        y += 1