def solution(a, b):
    answer = 0
    div = 2
    while div <= min(a, b):
        if a % div == 0 and b % div == 0:
            while a % div == 0 and b % div == 0:
                a = a // div
                b = b // div
        div += 1
    
    div = 2
    while div <= b:
        if b % div == 0:
            if div != 2 and div != 5:
                return 2
            while b % div == 0:
                b = b // div
        div += 1

    return 1